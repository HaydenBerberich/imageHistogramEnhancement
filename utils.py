import numpy as np

# Function to read a histogram from a file
def read_histogram_file(histogram_file):
    with open(histogram_file, 'r') as file:
        hist = np.array([float(line.strip()) for line in file], dtype=float)
    if len(hist) != 256:
        raise ValueError("Histogram file must contain 256 lines")
    return hist