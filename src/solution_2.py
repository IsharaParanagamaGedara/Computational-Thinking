def calculate_average_of_max_heights(readings):
    max_values = []
    for reading in readings:
        max_height = reading[0][0]
        for row in reading:
            for value in row:
                if value > max_height:
                    max_height = value
        max_values.append(max_height)
    return sum(max_values) / len(max_values)

# ---- Example Run ----
reading1 = [
    [0.67, 0.27, 0.67, 3.04, 0.5, 1.25, 0.37, 1.56],
    [0.13, 1.6, 1.23, 2.11, 3.11, 0.11, 1.56, 2.56],
    [0.33, 3.2, 2.1, 2.24, 3.0, 1.2, 1.44, 2.1],
    [0.88, 0.82, 0.81, 0.74, 0.8, 0.9, 1.22, 2.2],
    [1.56, 1.56, 1.56, 1.56, 3.2, 2.1, 2.24, 3.0],
    [2.56, 2.56, 2.56, 2.56, 0.81, 0.74, 0.8, 0.9],
    [2.1, 2.1, 2.1, 2.1, 1.56, 1.56, 3.2, 2.1],
    [2.2, 2.2, 2.2, 2.2, 3.2, 2.1, 2.24, 3.0]
]

reading2 = [
    [0.5, 1.2, 2.3, 0.7, 1.5, 0.8, 2.0, 1.1],
    [1.6, 1.8, 2.5, 2.9, 3.0, 1.1, 1.2, 0.6],
    [0.4, 0.9, 0.6, 2.2, 1.7, 1.3, 0.8, 0.1],
    [0.2, 2.1, 1.1, 2.2, 1.0, 2.3, 1.6, 2.9],
    [0.3, 1.9, 2.5, 2.2, 1.8, 1.7, 0.6, 1.9],
    [1.7, 0.6, 2.8, 3.0, 0.5, 2.4, 1.0, 1.9],
    [2.2, 1.1, 0.5, 1.9, 2.4, 2.2, 1.1, 1.7],
    [1.0, 1.3, 1.6, 1.9, 2.1, 2.2, 2.4, 2.5]
]

all_readings = [reading1, reading2]

average = calculate_average_of_max_heights(all_readings)
print("Average of maximum heights =", average)
