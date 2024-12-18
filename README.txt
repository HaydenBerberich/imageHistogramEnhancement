usage: main.py [-h] [-m {1,2,3}] imagefile [histogram_file]

Histogram Equalization and Matching

positional arguments:
  imagefile       Path to the input image file
  histogram_file  Path to the histogram file (Mode 2 or 3)

options:
  -h, --help      show this help message and exit
  -m {1,2,3}      Mode: 1=Equalization, 2=Matching with image, 3=Matching with file