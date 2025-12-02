# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 11:21:05 2025

@author: abkle
"""
import numpy as np

filepath= 'input_day1.txt'
with open(filepath, 'r') as f:
    movements = f.readlines()

dial = np.arange(0,100)
print("Dial starting position: "+str(dial[50]))

# movements = ['L168','L430','R348','L305','R360','L355','L201','L199','R114','L1082']
# movements = ['L168','L130','R148','L105','R160','L155','L101','L199','R114','L182']


num_crossings=0
num_rotations = 0
dial_at_zero = 0
for turn in range(len(movements)):
    direction = movements[turn][0]
    clicks = int(movements[turn][1:])
    
    #Calculate number of full rotations in which a 0 crossing occurs
    full_rotations = np.floor(clicks/100)
    num_rotations += full_rotations

    #Find starting index of 0 marker
    zero_index = np.where(dial==0)[0][0]
    print("Zero is at index "+str(zero_index))
    if direction == 'L':  
        if zero_index < 50:
            gap = 50-zero_index
        elif zero_index >50:
            gap = 150-zero_index
        else:
            gap = 100

        print("Gap is "+str(gap)+" with "+str(np.mod(clicks,100))+" clicks remaining")
        if gap<=np.mod(clicks, 100):
            zero_crossing = 1
            print("Flagged a zero crossing")
        else:
            zero_crossing = 0            

        dial = np.roll(dial,clicks)
        print("Left "+str(clicks)+" clicks to " +str(dial[50])+" with "+str(full_rotations)+" full rotations")
        if dial[50] == 0:
            dial_at_zero+=1
            # full_rotations = max(full_rotations-1, 0)

    elif direction == 'R':
        if zero_index<50:
            gap = 50+zero_index
        elif zero_index>50:
            gap = zero_index-50
        else:
            gap = 100

        print("Gap is "+str(gap)+" with "+str(np.mod(clicks,100))+" clicks remaining")
        if gap<=np.mod(clicks, 100):
            zero_crossing = 1
            print("Flagged a zero crossing")
        else:
            zero_crossing = 0                

        dial = np.roll(dial,-clicks)
        print("Right "+str(clicks)+" clicks to " +str(dial[50])+" with "+str(full_rotations)+" full rotations")
        if dial[50] == 0:
            dial_at_zero+=1
            # full_rotations = max(full_rotations-1, 0)

    else:
        print("Invalid Dial Direction")
    print('\n')
    num_crossings = num_crossings+full_rotations+zero_crossing
