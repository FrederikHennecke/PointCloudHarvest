import serial
import time

import pyrealsense2 as rs
import numpy as np
import cv2
import record


def write_message(string: str, ser: serial.Serial):
    if not string:
        return
    try:
        string = string.encode("utf_8")
        ser.write(string)
    except Exception as error:
        print("error sending message: ", error)


if __name__ == '__main__':
    # if connected via serial Pin(RX, TX)
    ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)  # 9600 is baud rate(must be same with that of NodeMCU)
    ser.flush()
    rec = record.recorder()
    while True:
        try:
            line = ser.readline().decode("UTF-8").strip()
            if line:
                print(line)
                if line.strip() == "stop":
                    rec.stop()
                    write_message("f", ser)
                else:
                    print("received: ", line)
                    if line.strip().startswith("f_"):
                        rec.start(line.strip())
                    else:
                        print("error parsing line")
                        rec.stop()
        except:
            print("Error while parsing message")
        time.sleep(1)  # delay of 1 second
