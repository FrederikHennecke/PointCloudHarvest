## Data Folder - Point Cloud Files

This folder contains point cloud files in the `.ply` format, representing 3D scans of polygons with varying numbers of edges. Each polygon was recorded multiple times to capture different iterations of the same shape under slightly varying conditions.

### File Naming Convention:
Each file is named using the following pattern:

```
n_m.ply
```

- **n**: The number of edges of the polygon used for the recording. This corresponds to the shape captured in the point cloud. For example:
  - `1`: Represents a single point.
  - `3`: Represents a triangle.
  - `6`: Represents a hexagon.
  
- **m**: The iteration number of the recording. Each polygon was recorded multiple times (with `m=3`), capturing the same polygon in different frames or slightly altered conditions. For example:
  - `1`: First recording of the polygon.
  - `2`: Second recording of the same polygon.
  - `3`: Third recording of the same polygon.

  
### Reconstruction:
Each file was created with the default settings found in `reconstruction_system/`