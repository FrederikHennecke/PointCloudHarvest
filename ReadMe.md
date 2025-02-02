# PointCloudHarvest (FarmBot Stereo-Vision Camera Module for Leaf Angle Calculation)

## Motivation
Leaf inclination angles (LIA) are crucial for regulating various processes within the plant carbon–water–energy nexus. In agriculture, these processes include photosynthesis, leaf temperature, plant growth, and the microclimate within the canopy. Despite its significance, LIA remains one of the most understudied plant functional traits due to the difficulty of measuring it accurately, particularly at short temporal intervals. In optical remote sensing, LIA is a key factor influencing spectral variability, which directly impacts the robustness of empirical models. We developed a novel and automated approach to capture 3D point clouds of small crops (e.g., sugar beet), enabling precise determination of LIA from the generated data. Our system, controlled by publicly available code, allows for customizable capture intervals and positions. The method was validated using a 3D-printed sugar beet model with known LIA, demonstrating its potential for advancing plant trait studies.

![farmbot](images/fig1_farmbot.png)

This project implements a module for the FarmBot that uses a stereo-vision camera to take point clouds of sugar beet plants and calculate their leaf angles. The module consists of scripts for recording plant data and generating point clouds from these recordings.

## Project Structure

- [`record/`](record/): Contains Python for recording the plants.
- [`reconstruction_system/`](reconstruction_system/): Contains Python files for creating point clouds from the recordings.
- [`farmbot_files`](farmbot_files/): Contains LUA files. Add the file to the FarmBot web interface.
- [`data/`](data/): Contains example point clouds each generated with this project.
- [`images/`](images/): Contains images used in this repository.
- [`printing_files/`](printing_files/): Contains CAD files used for the project. May be used to 3d print the camera bracket.

## Build Instructions
See [`hardware-setup.md`](hardware-setup.md)).

## Installation

Each folder ([`record/`](record/), [`reconstruction_system/`](reconstruction_system/), [`farmbot_files`](farmbot_files/)) has it's own installation instructions.

## Usage

### Recording Plant Data

- Navigate to the [`record/`](record/) directory and run the appropriate scripts on the camera module (Raspberry Pi).
- Navigate to the [`farmbot_files`](farmbot_files/) directory and copy the LUA file to the farmbot web interface.

### Generating Point Clouds

Navigate to the [`reconstruction_system/`](reconstruction_system/) directory and run the scripts to create point clouds from the recordings.

## Acknowledgements

Many files from the [Open3D documentation](http://www.open3d.org/docs/release/) were used in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

Please cite [our work](https://doi.org/10.1016/j.mex.2025.103169) if you use this software.
```bibtex
@article{Hennecke_Modification_of_an_2025,
    author  = {Hennecke, Frederik and Bömer, Jonas and Heim, René H.J.},
    doi     = {10.1016/j.mex.2025.103169},
    journal = {MethodsX},
    month   = jan,
    title   = {{Modification of an Automated Precision Farming Robot for High Temporal Resolution Measurement of Leaf Angle Dynamics using Stereo Vision}},
    url     = {http://dx.doi.org/10.1016/j.mex.2025.103169},
    year    = {2025}
}
```