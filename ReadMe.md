# PointCloudHarvest (FarmBot Stereo-Vision Camera Module for Leaf Angle Calculation)

This project implements a module for the FarmBot that uses a stereo-vision camera to take point clouds of sugar beet plants and calculate their leaf angles. The module consists of scripts for recording plant data and generating point clouds from these recordings.

## Project Structure

- `record/`: Contains Python for recording the plants.
- `reconstruction_system/`: Contains Python files for creating point clouds from the recordings.
- `farmbot_files/`: Contains LUA files. Add the file to the FarmBot web interface.
- `data/`: Contains example point clouds each generated with this project.

## Installation

Each folder (`record/`, `reconstruction_system/`, `farmbot_files/`) has it's own installation instructions.

## Usage

### Recording Plant Data

- Navigate to the `record/` directory and run the appropriate scripts on the camera module (Raspberry Pi).
- Navigate to the `farmbot_files` directory and copy the LUA file to the farmbot web interface.

### Generating Point Clouds

Navigate to the `reconstruction_system/` directory and run the scripts to create point clouds from the recordings.

## Acknowledgements

Many files from the [Open3D documentation](http://www.open3d.org/docs/release/) were used in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
