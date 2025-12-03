# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 10:43:08 2025

@author: abkle
"""
import time
filepath= 'input_day3.txt'
with open(filepath, 'r') as f:
    banks = f.read().splitlines()
    
#Test input
# banks = ['987654321111111', '811111111111119', '234234234234278', '818181911112111']

#%% Part 1
cumulative_sum = 0
for bank in banks:
    print("Bank "+bank)
    
    for i in range(9,0,-1):
        first_digit = str(i)
        first_ind = bank.find(first_digit, 0, len(bank)-1)
        if first_ind != -1:
            break
    
    for j in range(9,0,-1):
        second_digit = str(j)
        second_ind = bank.find(second_digit, first_ind+1)
        if second_ind != -1:
            break
    
    joltage = first_digit+second_digit
    print("Joltage "+joltage)
    cumulative_sum += int(joltage)
    
print("The answer to Part 1 is: "+str(cumulative_sum))

#%% Part 2 (and part 1)
num_batteries = 12
tic = time.time()
cumulative_sum = 0
for bank in banks:
    # print("Bank "+bank)
 
    joltage = ''
    digit_ind = -1
    for digit in range(num_batteries):
        for i in range(9,0,-1): #Search for each value, prioritizing highest value
            character = str(i)
            ind = bank.find(character, digit_ind+1, len(bank)-num_batteries+digit+1) #Find the highest value which will not make the number too short.
            if ind!=-1:
                digit_ind = ind #update start index for next digit
                break
        joltage = joltage+character
    print("Joltage "+joltage)
    cumulative_sum += int(joltage)

toc = time.time()

print("The answer to Part 2 is: "+str(cumulative_sum))
print("Calculation took "+str(toc-tic)+" s")

