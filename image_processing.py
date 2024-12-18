import cv2
import numpy as np

# Function to read an image as a grayscale image
def read_image(imagefile):
    image = cv2.imread(imagefile, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Image not found or not a grayscale image")
    return image

# Function to compute the histogram of an image
def compute_histogram(image):
    hist = np.zeros(256, dtype=int)
    for pixel in image.flatten():
        hist[pixel] += 1
    return hist

# Function to perform histogram equalization
def histogram_equalization(image):
    hist = compute_histogram(image)
    cdf = hist.cumsum()
    cdf_normalized = cdf * 255 / cdf[-1]
    equalized_image = cdf_normalized[image]
    return equalized_image.astype(np.uint8)

# Function to perform histogram matching using a reference histogram
def histogram_matching(image, reference_hist):
    hist = compute_histogram(image)
    cdf = hist.cumsum()
    cdf_normalized = cdf * 255 / cdf[-1]
    
    ref_cdf = reference_hist.cumsum()
    ref_cdf_normalized = ref_cdf * 255 / ref_cdf[-1]
    
    mapping = np.zeros(256, dtype=np.uint8)
    for i in range(256):
        diff = np.abs(ref_cdf_normalized - cdf_normalized[i])
        mapping[i] = np.argmin(diff)
    
    matched_image = mapping[image]
    return matched_image

# Function to compute mean, median, and variance of a histogram
def compute_histogram_statistics(hist):
    total_pixels = np.sum(hist)
    values = np.arange(256)
    
    mean = np.sum(values * hist) / total_pixels
    
    cumulative_hist = np.cumsum(hist)
    median_index = np.searchsorted(cumulative_hist, total_pixels / 2)
    median = values[median_index]
    
    variance = np.sum(((values - mean) ** 2) * hist) / total_pixels
    
    return mean, median, variance