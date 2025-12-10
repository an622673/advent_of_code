# advent_of_code
Master Repository for my submissions to Advent of Code

## 2025 ##
- Day 1: day1_sol.py - Not very happy with this solution, as it was more trial and error than careful planning and uses too many if statements to cover all cases. 
Started by solving Part 2 since I apparently can't read carefully. Good way to wake up the brain, and I realized that I probably shouldn't be using numpy.  
- Day 2: day2_sol.py - Part 1 and Part 2 could be merged, but I was happy with the solution for manually checking strings, and learning about the exchange between int and str within a list.
I like to think of this as an elegant brute force - break each of the strings which could possibly be repeated into their substring segments, Frankenstein them together and compare with the original. 
There only had to be one method of error handling, when IDs such as 222222 fit the invalid criteria multiple times and are therefore counted too much. Sets are useful.
- Day 3: day3_sol.py - This is my favorite so far. The part 2 solution is comparatively fast and efficient, and should work for any number of batteries (so part 1 as well).
However, I spent way more time than I needed realizing that .readlines() imports the newline character, which really messed up my exclusion of digits that are too close to the end.
- Day 4: Solution is good and gave me a chance to use some code that is actually relevant to my degree, which was nice. Unfortunately I am not good at visualization, 
because I think this would be a very illustrative one. Maybe I will revisit in the future.
- Day 5: Destructive lists are so good, and yet so bad. I spent about 30 minutes debugging and seeing great logical outputs before adding the max() to stop overwriting the original stop index of the range.
Had to write my own test case for the first time to see the behavior. 
- Day 6: Today I learned that casting a string to int() in Python will succeed regardless of if it is padded with spaces at the beginning or the end. 
I ended up rewriting my part 1 solution to produce a unified output. Cephalopod math is ridiculous BTW.


