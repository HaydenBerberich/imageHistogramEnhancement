# Hayden Berberich
# 10-26-2024

import sys
from arguments import parse_arguments
from image_processing import read_image, histogram_equalization, histogram_matching, compute_histogram, compute_histogram_statistics
from utils import read_histogram_file
import cv2

def main():
    args = parse_arguments()
    
    try:
        # Read the input image
        image = read_image(args.imagefile)
        
        # Compute the histogram of the input image
        input_hist = compute_histogram(image)
        
        # Compute and print the statistics of the input histogram
        mean, median, variance = compute_histogram_statistics(input_hist)
        print(f"Input Image - Mean: {mean}, Median: {median}, Variance: {variance}")
        
        # Perform the selected operation based on the mode
        if args.m == 1:
            result_image = histogram_equalization(image)
        elif args.m == 2:
            reference_image = read_image(args.histogram_file)
            reference_hist = compute_histogram(reference_image)
            
            # Compute and print the statistics of the reference histogram
            mean, median, variance = compute_histogram_statistics(reference_hist)
            print(f"Reference Image - Mean: {mean}, Median: {median}, Variance: {variance}")
            
            result_image = histogram_matching(image, reference_hist)
        elif args.m == 3:
            specified_hist = read_histogram_file(args.histogram_file)
            
            # Compute and print the statistics of the specified histogram
            mean, median, variance = compute_histogram_statistics(specified_hist)
            print(f"Specified Histogram - Mean: {mean}, Median: {median}, Variance: {variance}")
            
            result_image = histogram_matching(image, specified_hist)
        
        # Compute the histogram of the result image
        result_hist = compute_histogram(result_image)
        
        # Compute and print the statistics of the result histogram
        mean, median, variance = compute_histogram_statistics(result_hist)
        print(f"Result Image - Mean: {mean}, Median: {median}, Variance: {variance}")
        
        # Display the result image
        cv2.imshow('Result Image', result_image)
        cv2.waitKey(0)  # Wait for a key press to close the window
        cv2.destroyAllWindows()  # Close the window after the key press
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()