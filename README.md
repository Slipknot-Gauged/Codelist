# README

## 1. System Requirements

### All software dependencies and operating systems (including version numbers)
- **Python**: Version 3.9
- **Matlab**: Version R2020a or later
- **Wolfram Mathematica**: Version 13.3 or later
- **Microsoft Excel**: Version 2021 or later

### Versions the software has been tested on
- The software has been tested on Windows 11, 64-bit.

### Any required non-standard hardware
- No non-standard hardware is required.

## 2. Installation Guide

### Instructions
#### Python Environment:
- Install Python from [Python.org](https://www.python.org/downloads/).
#### Matlab:
- Install Matlab from [MathWorks](https://www.mathworks.com/products/matlab.html).
#### Wolfram Mathematica:
- Install Wolfram Mathematica from [Wolfram](https://www.wolfram.com/mathematica/).
#### Microsoft Excel:
- Install Microsoft Excel from [Microsoft](https://www.microsoft.com/en-us/microsoft-365/excel).

### Typical install time on a "normal" desktop computer
- Python environment setup: Approximately 10 minutes
- Matlab installation: Approximately 30 minutes
- Wolfram Mathematica installation: Approximately 20 minutes
- Microsoft Excel installation: Approximately 10 minutes

## 3. Demo

### Instructions to run on data
#### Data Processing:
- Open `DataProcess.m` in Matlab in the folder "Data-Process".
- Ensure `DataSet.xlsx` is in the same directory, and change its file name as necessary.
- Run the Matlab script to process the data.
#### Wolfram Mathematica Calculations:
- Open `Stage-1.nb` and `Stage-2.nb` in Wolfram Mathematica in the folder "Theoretical-Output".
- Execute the notebooks to reproduce the calculations in Fig. 2d. Ensure all the cells are evaluated.
#### Hardware Configuration:
- Open `cable_thread.py` in Python in the folder "Force-measurement-Device".
- Run the script to configure hardware as described in Supplementary Fig. 6.
- Follow the instructions and the `README.md` file in this folder.

### Expected output
- The output from `DataProcess.m` will be a processed dataset ready for further analysis.
- The Wolfram Mathematica notebooks will generate theoretical results as shown in Fig. 2d.
- The Python script will output configuration details relevant to Supplementary Fig. 6.

### Expected run time for demo on a "normal" desktop computer
- Data Processing in Matlab: Approximately 5 seconds
- Calculations in Wolfram Mathematica: Approximately 30 minutes (real-time output and a progress bar are included during evaluation).
- Hardware Configuration in Python: Approximately 2 minutes

## 4. Instructions for Use

### How to run the software on your data
#### Data Processing:
- Place your dataset in the same format as `DataSet.xlsx`.
- Modify `DataProcess.m` if necessary to accommodate changes in data structure.
- Run `DataProcess.m` in Matlab.
#### Calculations:
- Adjust the Wolfram Mathematica notebooks if additional parameters or different data are used.
- Execute the notebooks to perform calculations.
#### Hardware Configuration:
- Update `cable_thread.py` with your specific hardware details if different from those described in Supplementary Fig. 6.
- Run the Python script.

## 5. Vision-based sliputure and slipknot detection system
-Due to storage limitations, the code and training dataset related to the vision-based sliputure and slipknot detection system have been made available on our [project website](https://sites.google.com/view/slipknotnet). 

### (OPTIONAL) Reproduction instructions
- To reproduce all quantitative results in the manuscript, ensure all software versions and dependencies match those listed in the system requirements.
- Follow the demo instructions precisely, using the provided dataset and scripts.


