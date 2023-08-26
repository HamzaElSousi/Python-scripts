# This scripts is designed by Hamza El Sousi
# Version 1.0
# How to reach me: 

"""
Computer Engineer - Computer Science: Hamza El Sousi
Cell: 613 263 0255
Email: hamza.sousi1998@gmail.com
"""

import matplotlib.pyplot as plt

# Function to get numeric inputs from the user
def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid numeric value.")

# Function to create a line plot
def create_line_plot(x, y):
    plt.plot(x, y, marker='o')
    plt.title('Simple Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

# Function to create a bar chart
def create_bar_chart(x, y):
    plt.bar(x, y)
    plt.title('Simple Bar Chart')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

# Function to create a scatter plot
def create_scatter_plot(x, y):
    plt.scatter(x, y, color='red', marker='o', label='Data Points')
    plt.title('Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.show()

# Function to create a histogram
# Function to create a histogram
def create_histogram(data):
    plt.hist(data, bins=10, edgecolor='black')
    plt.title('Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

# Function to create a pie chart
def create_pie_chart(labels, y):
    plt.pie(y, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Pie Chart')
    plt.show()

# Function to create subplots
def create_subplots(x, y, labels):
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes[0, 0].plot(x, y, marker='o')
    axes[0, 0].set_title('Line Plot')

    axes[0, 1].bar(x, y)
    axes[0, 1].set_title('Bar Chart')

    axes[1, 0].scatter(x, y, color='red', marker='o')
    axes[1, 0].set_title('Scatter Plot')

    axes[1, 1].pie(y, labels=labels, autopct='%1.1f%%', startangle=90)
    axes[1, 1].set_title('Pie Chart')

    plt.tight_layout()
    plt.show()

# Function to collect numeric inputs from the user
def get_user_inputs():
    num_inputs = int(input("Enter the number of data points: "))
    data = []
    for i in range(num_inputs):
        value = get_numeric_input(f"Enter data point {i + 1}: ")
        data.append(value)
    return data

# Main program
data = get_user_inputs()

# You can choose which type of plot you want to create based on user input
# For example, if the user wants a line plot:
create_line_plot(range(1, len(data) + 1), data)

# If the user wants a bar chart:
create_bar_chart(range(1, len(data) + 1), data)

# If the user wants a Scatter plot chart:
create_scatter_plot(range(1, len(data) + 1), data)

# If the user wants a Histogram chart:
create_histogram(data)


# If the user wants a Pie chart:
#create_pie_chart(range(1, len(data) + 1), data)
create_pie_chart([f'Data Point {i+1}' for i in range(len(data))], data)

# If the user wants a Dashboard of subplots:
create_subplots(range(1, len(data) + 1), data, ["Label 1", "Label 2", ...])

# Similarly, you can call other functions for different types of plots.


# Remove the """ from bellow and end of script for a labled tempreture and humidity grapher

"""
# Function to create line plot with timestamps
def create_line_plot_with_timestamps(timestamps, data, title, x_label, y_label, color, label):
    plt.plot(timestamps, data, marker='o', color=color, label=label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Collect temperature and humidity data (You can change the labels but test the result)
timestamps = []
temperature = []
humidity = []

num_entries = int(input("Enter the number of data entries: "))

for i in range(num_entries):
    timestamp = input(f"Enter timestamp {i + 1}: ")
    temp = get_numeric_input(f"Enter temperature for {timestamp}: ")
    hum = get_numeric_input(f"Enter humidity for {timestamp}: ")

    timestamps.append(timestamp)
    temperature.append(temp)
    humidity.append(hum)

# Create line plot for temperature
create_line_plot_with_timestamps(timestamps, temperature, 'Temperature Readings', 'Timestamp', 'Temperature (°C)', 'green', 'Temperature')

# Create line plot for humidity
create_line_plot_with_timestamps(timestamps, humidity, 'Humidity Readings', 'Timestamp', 'Humidity (%)', 'red', 'Humidity')

"""
