# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 10:00:17 2025

@author: abkle
"""

filepath= 'input_day5.txt'

with open(filepath, 'r') as f:
    database = f.read().splitlines()

# database = ['3-5', '10-14', '16-20', '12-18','','1','5','8','11','17','32']

# database = ['3-55', '10-41', '160-164','10-41', '122-159','','1','5','8','11','17','32']

split_index = database.index('')



fresh_ingredients = database[0:split_index]
available_ingredients = database[split_index+1:]

number_fresh = 0
for ingredient in available_ingredients:
    ingredient_val = int(ingredient)
    for ID_range in fresh_ingredients:
        [start, stop] = ID_range.split('-')
        if (ingredient_val>=int(start) and ingredient_val<=int(stop)):
            number_fresh += 1
            # print("Ingredient "+ingredient+" safe in "+ID_range)
            break

searchable_indices = []
for ID_range in fresh_ingredients:
    # print("Fresh Ingredient Range "+ID_range)
    [start, stop] = ID_range.split('-')
    searchable_indices.append([int(start), int(stop)])
    
reference_ranges = sorted(searchable_indices)
ordered_ranges = sorted(searchable_indices)

# #Sort every range and eliminate exact duplicates
# ordered_ranges = sorted(set(tuple(element) for element in searchable_indices)) 

ind = 0
while ind < len(ordered_ranges):
    current_length = len(ordered_ranges)
    print("Checking Index: "+str(ind), "Current Length: "+str(current_length))
    #If the end of the current range is overlapping with the next range start
    if ordered_ranges[ind][1] >= ordered_ranges[ind+1][0]-1:
        #update the end of the current range to the end of the next range
        ordered_ranges[ind][1] = max(ordered_ranges[ind+1][1], ordered_ranges[ind][1])
        #Delete the duplicate values and re-evaluate the current updated range
        print("Removing range "+str(ordered_ranges[ind+1]))
        del ordered_ranges[ind+1]
        ind -= 1
    #stop if the iteration reaches the last value
    if ind+2 > current_length-2:
        print("Terminated at "+str(current_length-1)+" entries")
        break
    ind += 1
#%%
cumulative_sum = 0
for concatenated_range in ordered_ranges:
    cumulative_sum += (concatenated_range[1] - concatenated_range[0])+1

print("Part 2 answer is: "+str(cumulative_sum))
    
# for i in range(len(ordered_ranges)-1):
#     if ordered_ranges[i][1] >= ordered_ranges[i+1][0]-1:
#         ordered_ranges[i][1] = ordered_ranges[i+1][1]
#         ordered_ranges[i+1][0] = ordered_ranges[i][0]
