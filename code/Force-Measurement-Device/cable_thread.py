import argparse
import csv
import re
import threading
import time
from queue import Queue
from datetime import datetime

import numpy as np
import serial
from matplotlib import animation
import matplotlib
import matplotlib.pyplot as plt
from collections import deque


class Sensor:
    def __init__(self, port='COM4', baudrate=115200, timeout=2, period=60, buffer_size=2000, filename=''):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.period = period
        self.s = self.init_serial()
        self.reading_Set = []
        self.filename = filename
        self.buffer = deque(maxlen=buffer_size)
        self.baseline = self.collect_baseline(num_points=100)
        self.save = False

    def init_serial(self):
        try:
            ser = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            print(f"Successfully connect to serial port {self.port}")
            return ser
        except serial.SerialException as e:
            print(f"Error opening the serial port: {e}")
            return None

    def collect_baseline(self, num_points=200):
        """Collect an initial set of data points and calculate the baseline average."""
        baseline_data = []
        print("Collecting baseline data...")
        while len(baseline_data) < num_points:
            try:
                string = self.s.readline().decode('utf-8').strip()
                match = re.match(r"<(\d+)>", string)
                # print(f'match is {match}')
                if match:
                    force = int(match.group(1))
                    baseline_data.append(force)
            except KeyboardInterrupt:
                print("Baseline collection interrupted.")
                return None
        baseline_average = sum(baseline_data) / len(baseline_data)
        print(f"Baseline collection complete. Average: {baseline_average}")
        self.start_time = time.time()
        return baseline_average

    def measure(self, result_queue):
        while time.time() - self.start_time < self.period:
            try:
                # Read data from Arduino
                string = self.s.readline().decode('utf-8').strip()
                # Extract the value from the format <value>
                match = re.match(r"<(\d+)>", string)
                if match:
                    force = int(match.group(1))
                    if self.baseline is not None:
                        force -= self.baseline
                        if force < 0:
                            force = 0
                    print(f'current force is {force}')
                    self.reading_Set.append(force)
                    self.buffer.append(force)
                    result_queue.put(self.buffer)
            except KeyboardInterrupt:
                print("Measure fails...")
        else:
            self.save = True
            print(f'Begin to save the data')
            self.save_to_csv()

    def save_to_csv(self):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        max_f = max(self.reading_Set)
        filename = self.filename + f'{np.round(max_f,3)}N_' + f'{timestamp}.csv'
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['ColumnHeader'])  # Add your column header

            for item in self.reading_Set:
                csv_writer.writerow([item])  # Assuming each item is a single value
        print(f'File {filename} being created successfully')


class Visualization:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.measurements = []
        self.line, = self.ax.plot([], [], 'o-', label='Sensor Data')
        self.ax.legend()
        self.ax.set_title('Real-time Sensor Data Visualization')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Sensor Reading')

    def update(self, data_to_visualize):
        self.ax.clear()
        x = list(range(len(data_to_visualize)))
        self.ax.plot(x, data_to_visualize)

    def visualize(self, result_queue):
        try:
            while True:
                # Retrieve measurement data from the queue
                self.measurements = result_queue.get()
                # self.measurements.append(force)
                self.update(self.measurements)
                plt.pause(0.0001)  # Allow time for the plot to update
        except KeyboardInterrupt:
            print("Visualization stops...")


def worker(sensor, result_queue):
    sensor.measure(result_queue)


if __name__ == "__main__":
    matplotlib.use('TkAgg')

    # Argument parser
    parser = argparse.ArgumentParser(description='Sensor Data Collection and Visualization')
    parser.add_argument('--port', type=str, default='COM4', help='Serial port of the sensor')
    parser.add_argument('--baudrate', type=int, default=115200, help='Baud rate for serial communication')
    parser.add_argument('--period', type=int, default=16, help='Duration of the experiment in seconds')
    parser.add_argument('--buffer_size', type=int, default=1600, help='Size of the sliding window for visualization')
    parser.add_argument('--sample_no', type=str, default='Subject1', help='Sample number or identifier')
    parser.add_argument('--exp_no', type=int, default=6, help='Experiment number')

    args = parser.parse_args()

    filename = f'{args.sample_no}_Exp{args.exp_no}_'  # Filename based on sample number and experiment number
    # filename = f'{args.sample_no}_Exp{args.exp_no}(Control)_'  # Uncomment for control experiments

    sensor = Sensor(port=args.port, baudrate=args.baudrate, period=args.period, buffer_size=args.buffer_size,
                    filename=filename)
    visualization = Visualization()
    result_queue = Queue()

    # Start the sensor measurement threadq
    measure_thread = threading.Thread(target=worker, args=(sensor, result_queue))
    measure_thread.start()

    try:
        # Run the visualization in the main thread
        visualization.visualize(result_queue)
    except KeyboardInterrupt:
        print("Program terminated by user.")
