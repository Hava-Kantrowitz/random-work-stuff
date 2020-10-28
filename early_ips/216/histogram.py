#!/usr/bin/env python

import numpy as np
import tkinter as tk
import pandas as pd
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='test')
parser.add_argument('file_name',help='Required name of file')
args = parser.parse_args()

file_name = args.file_name

print("Making graph") 

data = pd.read_csv(file_name)
plt.xlabel('Seconds')
plt.title(file_name)
print("Making histogram")
plt.hist(data['duration'], bins=10)
print("saving") 
plt.savefig('durationpic.png')

