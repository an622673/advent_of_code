# -*- coding: utf-8 -*-
"""
Created on Tue Dec 2 13:45:53 2025

@author: abkle
"""

filename = 'input_day2.txt'

with open(filename, 'r') as f:
    master_list = f.read()
    
product_IDs = master_list.split(",")

#Test Sample input
# product_IDs = ["11-22", "95-115", "998-1012", "1188511880-1188511890", 
#                "222220-222224", "1698522-1698528", "446443-446449", 
#                "38593856-38593862", "565653-565659", "824824821-824824827",
#                "2121212118-2121212124"]

cumulative_value = 0
for ID_range in product_IDs:
    print("ID Range "+ID_range)
    [start, stop] = ID_range.split('-')
    ID_range = list(range(int(start),int(stop)+1))
    valid_IDs = 0
    invalid_strings= []

    for ID in ID_range:
        ID_string = str(ID)
        
        #Part 1
        # if (len(ID_string)%2) !=0: #Odd length strings cannot be repeated
        #     valid_IDs += 1
        # else: 
        #     half_ID = ID_string[0:len(ID_string)//2]
        #     try:
        #         index = ID_string.index(half_ID,len(half_ID),len(ID_string)+len(half_ID))
        #         cumulative_value += int(ID_string)
        #         # print("Invalid ID: "+ID_string)
        #     except ValueError:
        #         valid_IDs += 1
        
        #Part 2

        for i in range(1,len(ID_string)//2+1): #Iterate over all possible substring lengths
            if len(ID_string)%i == 0: #Only activate if substring can be repeated
                substring = ID_string[0:i]
                substring_repeated = substring*(len(ID_string)//i)
                if substring_repeated == ID_string:
                    invalid_strings.append(ID_string)
                    print("Invalid ID: "+ID_string)
                else:
                    valid_IDs += 1
            else:
                valid_IDs += 1
    invalid_strings = list(set(invalid_strings))
    print(invalid_strings)
    print("\n")
    cumulative_value += sum([int(x) for x in invalid_strings])
    # print(str(valid_IDs)+" Valid IDs out of "+str(len(ID_range))
print("Solution is: "+str(cumulative_value))