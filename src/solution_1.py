def calculate_average_of_max_heights(readings):
    """
    readings: list of 2D lists (each 8x8 matrix of plant heights)
    returns: average of maximum heights
    """
    max_values = []

    for reading in readings:
        max_height = reading[0][0]
        for row in reading:
            for value in row:
                if value > max_height:
                    max_height = value
        max_values.append(max_height)

    # Compute average
    average = sum(max_values) / len(max_values)
    return average


# ---- Example Run using Table 1 ----
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

# Suppose we only have 1 reading
all_readings = [reading1]

average = calculate_average_of_max_heights(all_readings)
print("Average of maximum heights =", average)
