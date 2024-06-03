![GitHub User's stars](https://img.shields.io/github/stars/hoseinnikkhah)
![GitHub forks](https://img.shields.io/github/forks/hoseinnikkhah/Time_Tracker)
![GitHub followers](https://img.shields.io/github/followers/hoseinnikkhah)

![Static Badge](https://img.shields.io/badge/Finished-Finished?style=flat&logo=github&logoColor=white&label=Status&color=green) ![GitHub License](https://img.shields.io/github/license/hoseinnikkhah/Time_Tracker)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/hoseinnikkhah/Time_Tracker) ![Static Badge](https://img.shields.io/badge/v-1.0.0-v?style=flat&logo=python&logoColor=yellow&label=python&color=yellow)


---

# Process Monitoring Tool

## Overview

The **Process Monitoring Tool** is a Python application designed to monitor the status and runtime of a specified process on a Windows system. It continuously checks whether a particular process is running and records the duration for which it remains active.

## Purpose

This tool serves as a utility for users who need to track the execution time of a specific process, such as a software application or background service. It provides real-time updates on the status of the process and logs the start and end times along with the elapsed duration.

## Features

- **Real-time Monitoring**: The tool actively monitors the specified process and updates the user interface with its current status.
  
- **Elapsed Time Display**: It displays the elapsed time since the start of the monitored process, both in seconds and hours, for easy tracking.

- **Data Logging**: The tool records the start time, end time, and elapsed duration of the process in a CSV file named `data_sheet.csv` for future reference and analysis.

## Usage

1. **Specify Process**: Set the `PID` variable in the code to the name of the process you want to monitor. For example, `"AfterFX.exe"`.

2. **Run the Application**:
   
    - **Windows**:
        - Open Command Prompt (CMD).
        - Navigate to the directory where the code is saved using the `cd` command. For example:
          ```
          cd path/to/directory
          ```
        - Run the script using the following command:
          ```
          python monitor_afterfx.py
          ```

    - **Linux/Mac**:
        - Open Terminal.
        - Navigate to the directory where the code is saved using the `cd` command. For example:
          ```
          cd path/to/directory
          ```
        - Run the script using the following command:
          ```
          python3 monitor_afterfx.py
          ```

3. **Monitor Process**: The application interface will display the current status of the specified process and the elapsed time since it started.

4. **Review Data**: Check the `data_sheet.csv` file generated by the tool to analyze the runtime statistics of the monitored process.

## Dependencies

- **Python 3.x**
- **Tkinter**: Python's standard GUI toolkit
- **psutil**: A cross-platform library for retrieving information on running processes and system utilization

## How It Works

The tool utilizes the `psutil` library to iterate through the list of running processes and check if the specified process is active. It updates the user interface accordingly and calculates the elapsed time if the process is running. The data is logged into a CSV file using Python's built-in `csv` module.

## License

This project is licensed under the MIT License 

---
