#!/usr/bin/env python
import rebound, argparse, os
import numpy as np

# Args
parser = argparse.ArgumentParser(description='Simulate the trajectory for the specified Svea family asteroid')
parser.add_argument('integers', metavar='no', type=int, nargs='+', help='an integer specifying the binary file used')
args = parser.parse_args()
no = args.integers[0]

# Args