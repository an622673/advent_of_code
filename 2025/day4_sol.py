# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 12:53:46 2025

@author: abkle
"""

import numpy as np
from scipy.signal import correlate2d
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
filepath= 'input_day4.txt'

with open(filepath, 'r') as f:
    grid = f.read().splitlines()
    
# grid = ['..@@.@@@@.','@@@.@.@.@@','@@@@@.@.@@','@.@@@@..@.','@@.@@@@.@@','.@@@@@@@.@',
#         '.@.@.@.@@@','@.@@@.@@@@','.@@@@@@@@.','@.@.@@@.@.']

#Transcribe array to numpy
numpy_grid = np.zeros((len(grid), len(grid[0]))) 
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] =='@':
            numpy_grid[i,j] = 1

#Define kernel 
kernel = np.array([[1,1,1], [1,0,1], [1,1,1]])

total_accessible = 1
total_removed = 0
tic = time.time_ns()
while total_accessible > 0:
    #Calculate number of neighbors using correlation
    neighbors = correlate2d(numpy_grid, kernel, mode="same")
    accessible_rolls = np.multiply(neighbors<4, numpy_grid==1)
    total_accessible = np.sum(accessible_rolls)
    print("There are "+str(total_accessible)+" rolls that can be accessed")
    
    numpy_grid[accessible_rolls] = 0
    total_removed += total_accessible
toc = time.time_ns()    
print(str(total_removed)+" rolls can be removed")
print("Calculation took "+str((toc-tic)/1e6)+" ms")
