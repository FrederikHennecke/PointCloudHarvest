# RealSense Angle Measurement Software

This software is designed to capture and analyze angles using a RealSense camera on a Raspberry Pi.

## Prerequisites

### Librealsense

Librealsense is a cross-platform library for capturing data from Intel RealSense depth cameras.

To install Librealsense, follow these steps:

1. Install the prerequisites:

   - On Ubuntu:
     ```bash
     sudo apt-get update && sudo apt-get upgrade
     sudo apt-get install git cmake libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev
     ```

   - On Windows:
     Download and install [Visual Studio](https://visualstudio.microsoft.com/) and [CMake](https://cmake.org/download/).

2. Clone the librealsense repository:

   ```bash
   git clone https://github.com/IntelRealSense/librealsense.git
   cd librealsense
   ```

3. Build and install the library:

   - On Ubuntu:
     ```bash
     mkdir build && cd build
     cmake ../ -DBUILD_EXAMPLES=true
     make && sudo make install
     ```

   - On Windows:
     Follow the instructions in the `librealsense` [documentation](https://github.com/IntelRealSense/librealsense/blob/master/doc/installation_windows.md).

### Python

1. **Install Python 3**: Ensure Python 3 is installed on your Raspberry Pi.

2. **Install RealSense Library**:
   - You need to install the RealSense library (`librealsense2`) on your Raspberry Pi.
   - Follow the official [Intel RealSense installation guide](https://github.com/IntelRealSense/librealsense/blob/master/doc/installation.md) for instructions specific to your platform.

3. **Install Python Dependencies**:
   - After installing `librealsense2`, install the required Python dependencies. This includes the RealSense Python wrapper.

   ```bash
   pip install opencv-python
   pip install pyrealsense2
   ```

## Installation

1. **Clone the Repository**:
   - Download the software to your Raspberry Pi by cloning the repository or copying the files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Software**:
   - To start capturing and analyzing angles, run the `main.py` script.

   ```bash
   python3 main.py
   ```

## Usage

Once the software is running, it will automatically begin capturing depth images, whenever it gets a signal via UART.

## Troubleshooting

- Ensure that the RealSense camera is properly connected to the Raspberry Pi.
- Make sure `librealsense2` and `pyrealsense2` are correctly installed.
- If you encounter any errors, check the dependencies and ensure all required libraries are installed.

