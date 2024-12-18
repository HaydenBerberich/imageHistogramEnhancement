import argparse

# Function to parse command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description='Histogram Equalization and Matching')
    parser.add_argument('imagefile', type=str, help='Path to the input image file')
    parser.add_argument('histogram_file', type=str, nargs='?', help='Path to the histogram file (Mode 2 or 3)')
    parser.add_argument('-m', type=int, choices=[1, 2, 3], default=1, help='Mode: 1=Equalization, 2=Matching with image, 3=Matching with file')
    
    args = parser.parse_args()
    
    # Error handling for missing histogram_file in mode 2 or 3
    if args.m == 2 and not args.histogram_file:
        parser.error("Mode 2 requires a reference image.")
    elif args.m == 3 and not args.histogram_file:
        parser.error("Mode 3 requires a histogram file.")
    
    return args