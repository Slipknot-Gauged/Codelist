% Read the data from the Excel file
data = xlsread('path_to_file-DataSet.xlsx'); % replace with actual file path

% Calculate the average (mean)
average_value = mean(data);

% Calculate the standard deviation (STDEV.S)
stddev_value = std(data);

% Display the results
fprintf('Average: %.6f\n', average_value);
fprintf('Standard Deviation: %.6f\n', stddev_value);
