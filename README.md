# advent_of_code
Master Repository for my submissions to Advent of Code

## 2025 ##
- Day 1: day1_sol.py - Not very happy with this solution, as it was more trial and error than careful planning and uses too many if statements to cover all cases. 
Started by solving Part 2 since I apparently can't read carefully. Good way to wake up the brain, and I realized that I probably shouldn't be using numpy.  
- Day 2: day2_sol.py - Part 1 and Part 2 could be merged, but I was happy with the solution for manually checking strings, and learning about the exchange between int and str within a list.
I like to think of this as an elegant brute force - break each of the strings which could possibly be repeated into their substring segments, Frankenstein them together and compare with the original. 
There only had to be one method of error handling, when IDs such as 222222 fit the invalid criteria multiple times and are therefore counted too much. Sets are useful.

