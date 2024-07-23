# Tension Force Measurement and Visualization

## Overview

This project consists of a Python program designed to record the tension force during suture operation with a loadcell connected via a serial port.
The code provide real-time and simultaneous force measurement and visualizion. The collected data is saved to a CSV file for further analysis.

## System Requirements
### Hardware requirements
This code requires only standard computer with Serial Port to support the tension force measurements from the loadcell

### Softward requirements
This code is designed for Windows, but also support macOS and Linux. The code have been tested on the following system:
-Windows: Win11

### Python Dependencies
Before running the program, ensure you have the following dependencies installed:

- Python 3.9
- `argparse`
- `csv`
- `re`
- `threading`
- `time`
- `queue`
- `datetime`
- `numpy`== 2.0.1
- `serial`
- `matplotlib`== 3.8.4
- `collections`
- `pyserial`== 3.5

### Installation Guide:
Install from the 'requirement.txt'

```bash
pip install -r requirement.txt 
```

## Usage
To run the program, use the example command line to specify the serial port and other parameters:

```bash
python main.py --port COM4 --baudrate 115200 --period 16 --buffer_size 1600 --sample_no 'Subject1' --exp_no 6
```
This would create a recording of 16 seconds for 6th trial of 'Subject1'


## Program Structure
### Sensor Class
Handles serial communication with the sensor, data collection, and saving data to a CSV file.
### Methods
- `__init__(self, port, baudrate, timeout, period, buffer_size, filename)`: Initializes the Sensor object with the specified parameters.
- `init_serial(self)`: Initializes the serial connection.
- `collect_baseline(self, num_points)`: Collects an initial set of data points and calculates the baseline average.
- `measure(self, result_queue)`: Measures data from the sensor and puts it into the result queue.
- `save_to_csv(self)`: Saves the collected data to a CSV file.


### Visualization Class
Manages real-time plotting of the sensor data.
### Methods
- `__init__(self)`: Initializes the Visualization object.
- `update(self, data_to_visualize)`: Updates the plot with new data.
- `visualize(self, result_queue)`: Visualizes the data in real-time by reading from the result queue.

