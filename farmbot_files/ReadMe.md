# FarmBot Point Cloud Recording

This guide explains how to use the `pointcloud.lua` script to record point clouds with your FarmBot system. Follow the steps below to set up and start recording.

## Prerequisites

1. **FarmBot System**: Ensure your FarmBot is set up and connected properly.
2. **FarmBot Account**: You should have access to the FarmBot interface (my.farm.bot).

## Installation

1. **Access FarmBot Interface**:
   - Log in to your FarmBot account at [my.farm.bot](https://my.farm.bot).

2. **Upload Lua Script**:
   - Navigate to **Sequences** within the FarmBot interface.
   - Copy and paste the contents of `pointcloud.lua` into a new sequence.

3. **Handle Script Length Limitations**:
   - Due to FarmBot's limitation on Lua file length (<=3000 symbols), a secondary file named `pointcloud_comments.lua` is provided.
   - This file includes comments and additional details that are not critical for execution but are helpful for understanding the script's purpose and usage.

## Running the Recording

To start recording point clouds, you can use one of the following methods:

### Method 1: Run Sequence Manually

1. Go to **Sequences** in the FarmBot interface.
2. Select the sequence you created with `pointcloud.lua`.
3. Click **Run Sequence** to start the recording.

### Method 2: Schedule Automatic Recording

1. Go to **Events** in the FarmBot interface.
2. Click **Add Event**.
3. Select the sequence you created with `pointcloud.lua`.
4. Set the desired interval for multiple recordings.
5. Save the event to schedule automatic recordings based on the interval you specified.

## Troubleshooting

- **Script Errors**: If you encounter issues, check that the Lua script has been correctly copied and that no parts are missing.
- **Script Length**: Ensure the `pointcloud.lua` file does not exceed 3000 symbols. The file `pointcloud_comments.lua` is only for documentation purposes.
- **Recording Issues**: Verify that the sequence is correctly set up and that your FarmBot is properly connected and calibrated.
