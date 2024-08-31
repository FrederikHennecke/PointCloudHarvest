import threading
import pyrealsense2 as rs
import numpy as np
import cv2
from os import makedirs
from os.path import exists, join, abspath
import shutil
import json

import sys

sys.path.append(abspath(__file__))


def make_clean_folder(path_folder):
    """
    delete folder and make a new one (to clean up old data)
    :param path_folder: file path
    :return:
    """
    if not exists(path_folder):
        makedirs(path_folder)
    else:
        shutil.rmtree(path_folder)
        makedirs(path_folder)


def save_intrinsic_as_json(filename, frame):
    """
    save the current intrinsics
    :param filename: JSON file path
    :param frame: realsense frame object to get the current intrinsics
    :return:
    """
    intrinsics = frame.profile.as_video_stream_profile().intrinsics
    with open(filename, 'w') as outfile:
        json.dump(
            {
                'width':
                    intrinsics.width,
                'height':
                    intrinsics.height,
                'intrinsic_matrix': [
                    intrinsics.fx, 0, 0, 0, intrinsics.fy, 0, intrinsics.ppx,
                    intrinsics.ppy, 1
                ]
            },
            outfile,
            indent=4)


class recorder:
    """
    class to start / stop recording RGBD images
    """

    def __init__(self):
        self.run = False
        self.thread = None

    def start(self, path_output="../dataset/"):
        """
        start recording RGBD images
        :param path_output: file path to save output
        :return:
        """
        if not self.run:
            self.run = True
            self.thread = threading.Thread(target=self._rec, kwargs={"path_output": path_output})
            self.thread.start()
        else:
            self.stop()
            self.start()

    def _rec(self, path_output, show_window=False):
        """
        :param path_output: file path to save output
        :param show_window: debug option to show currently seen depth image
        :return:
        """
        self.run = True

        path_depth = join(path_output, "depth")
        path_color = join(path_output, "color")

        # record imgs
        make_clean_folder(path_output)
        make_clean_folder(path_depth)
        make_clean_folder(path_color)

        # Create a pipeline
        pipeline = rs.pipeline()

        jsonObj = json.load(open("camSettings.json"))
        json_string = str(jsonObj["parameters"]).replace("'", '\"')

        # Create a config and configure the pipeline to stream
        #  different resolutions of color and depth streams
        config = rs.config()
        config.enable_stream(rs.stream.depth, int(jsonObj['viewer']['stream-width']),
                             int(jsonObj['viewer']['stream-height']),
                             rs.format.z16, int(jsonObj['viewer']['stream-fps']))
        config.enable_stream(rs.stream.color, int(jsonObj['viewer']['stream-width']),
                             int(jsonObj['viewer']['stream-height']),
                             rs.format.bgr8, int(jsonObj['viewer']['stream-fps']))
        cfg = pipeline.start(config)
        dev = cfg.get_device()

        advnc_mode = rs.rs400_advanced_mode(dev)
        advnc_mode.load_json(json_string)

        # Start streaming
        depth_sensor = cfg.get_device().first_depth_sensor()

        # Getting the depth sensor's depth scale (see rs-align example for explanation)
        depth_scale = depth_sensor.get_depth_scale()

        # We will not display the background of objects more than
        #  clipping_distance_in_meters meters away
        clipping_distance_in_meters = 3  # 3 meter
        clipping_distance = clipping_distance_in_meters / depth_scale

        # Create an align object
        # rs.align allows us to perform alignment of depth frames to others frames
        # The "align_to" is the stream type to which we plan to align depth frames.
        align_to = rs.stream.color
        align = rs.align(align_to)

        # Streaming loop
        frame_count = 0
        try:
            while True:
                # Get frameset of color and depth
                frames = pipeline.wait_for_frames()

                # Align the depth frame to color frame
                aligned_frames = align.process(frames)

                # Get aligned frames
                aligned_depth_frame = aligned_frames.get_depth_frame()
                color_frame = aligned_frames.get_color_frame()

                # Validate that both frames are valid
                if not aligned_depth_frame or not color_frame:
                    continue

                depth_image = np.asanyarray(aligned_depth_frame.get_data())
                color_image = np.asanyarray(color_frame.get_data())

                if frame_count == 0:
                    save_intrinsic_as_json(
                        join(path_output, "camera_intrinsic.json"),
                        color_frame)

                cv2.imwrite("%s/%06d.png" % (path_depth, frame_count), depth_image)
                cv2.imwrite("%s/%06d.jpg" % (path_color, frame_count), color_image)
                print("Saved color + depth image %06d" % frame_count)
                frame_count += 1

                # Remove background - Set pixels further than clipping_distance to grey
                grey_color = 153
                # depth image is 1 channel, color is 3 channels
                depth_image_3d = np.dstack((depth_image, depth_image, depth_image))
                bg_removed = np.where((depth_image_3d > clipping_distance) | \
                                      (depth_image_3d <= 0), grey_color, color_image)

                # Render images
                depth_colormap = cv2.applyColorMap(
                    cv2.convertScaleAbs(depth_image, alpha=0.09), cv2.COLORMAP_JET)
                images = np.hstack((bg_removed, depth_colormap))

                if show_window:
                    cv2.namedWindow('Recorder Realsense', cv2.WINDOW_AUTOSIZE)
                    cv2.imshow('Recorder Realsense', images)
                    cv2.waitKey(1)

                if not self.run:
                    cv2.destroyAllWindows()
                    break

        except Exception as e:
            print(e)
        finally:
            pipeline.stop()
            # send uart message

    def stop(self):
        """
        stop recording
        :return:
        """
        if self.run:
            self.run = False
            self.thread.join()  # Wait for the thread to finish


if __name__ == "__main__":
    app = recorder()

