# Open3D Reconstruction System

This software provides a flexible system for reconstructing 3D models from RGBD sequences using Open3D. You can control various stages of the reconstruction process through command-line arguments.

## Prerequisites

1. **Install Python 3**: Ensure Python 3 is installed on your system.

2. **Install Required Libraries**:
   - Install Open3D and other necessary Python libraries:

   ```bash
   pip install opencv-python
   pip install open3d
   ```
(See [here](https://www.open3d.org/docs/release/getting_started.html) for help using Open3D)
## Installation

1. **Clone the Repository**:
   - Download the software to your local machine:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the Software**:
   - If there are any additional setup steps or dependencies, follow the instructions provided in the repository.

## Usage

```bash
python3 main.py [OPTIONS]
```

### Available Arguments

- `--config`:
  - **Optional**: Path to the configuration file.
  - **Default**: `None`

- `--default_dataset`:
  - **Optional**: Dataset to be used if no config file is provided.
  - **Options**: `lounge`, `bedroom`, `jack_jack`
  - **Default**: `lounge`

- `--make`:
  - **Optional**: Generate fragments from the RGBD sequence.
  
- `--register`:
  - **Optional**: Register all fragments and detect loop closures.
  
- `--refine`:
  - **Optional**: Refine the rough registrations of fragments.
  
- `--integrate`:
  - **Optional**: Integrate the entire RGBD sequence to create the final mesh.
  
- `--slac`:
  - **Optional**: Run SLAC optimization on fragments (if using SLAC).
  
- `--slac_integrate`:
  - **Optional**: Integrate fragments using SLAC to create the final point cloud or mesh.
  
- `--debug_mode`:
  - **Optional**: Enable debug mode for detailed logs and troubleshooting.
  
- `--device`:
  - **Optional**: Select the processing device for SLAC and SLAC integration.
  - **Example**: `cpu:0`, `cuda:0`
  - **Default**: `cpu:0`
  
- `--multiple`:
  - **Optional**: Reconstruct multiple recordings from the specified dataset path.
  - **Example**: `../dataset/`

### Example Commands

1. **Run reconstruction with default settings**:

   ```bash
   python3 main.py --config config/realsense.json --make --register --refine --integrate
   ```

2. **Run reconstruction with SLAC optimization and GPU acceleration**:

   ```bash
   python3 main.py --config config/realsense.json --make --register --refine --integrate --slac --slac_integrate --device cuda:0
   ```

3. **Run reconstruction multiple times with given file path**:

   ```bash
   python run_system.py --config config/realsense.json --make --register --refine --integrate --slac --slac_integrate --multiple "../dataset/"
   ```

## Troubleshooting

- **Ensure all dependencies are installed**: Verify that Open3D and any additional libraries are correctly installed.
- **Check your dataset paths and config file**: Make sure paths are correctly specified and accessible.
- **Consult logs**: If encountering issues, review the debug logs if `--debug_mode` is enabled.


## Citation
Thanks to the Open3D project.
```bibtex
@article{Zhou2018,
    author    = {Qian-Yi Zhou and Jaesik Park and Vladlen Koltun},
    title     = {{Open3D}: {A} Modern Library for {3D} Data Processing},
    journal   = {arXiv:1801.09847},
    year      = {2018},
}```