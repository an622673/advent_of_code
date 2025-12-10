# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 15:57:30 2025

@author: abkle
"""
import time
#%% Import and Parse Data
filepath= 'input_day6.txt'
with open(filepath, 'r') as f:
    banks = f.read().splitlines()

operators_with_spaces = banks[-1]
operators = ['+', '*']
operator_indices = [i for i, x in enumerate(operators_with_spaces) if x in operators]

problem_inputs = []
for j in range(len(operator_indices)-1):
    problem = []
    for k in range(len(banks)-1):
        problem.append(banks[k][operator_indices[j]:operator_indices[j+1]-1])
    problem.append(operators_with_spaces[operator_indices[j]])
    problem_inputs.append(problem)
    
#append last value
last_problem = []
for k in range(len(banks)-1):
    last_problem.append(banks[k][operator_indices[-1]:])
last_problem.append(operators_with_spaces[operator_indices[-1]])
problem_inputs.append(last_problem)

#%% Define Math Functions

def human_tabulate(problem_values):
    if problem_values[-1] == "*":
        answer = 1
        for i in range(len(problem_values)-1):
            answer = answer*int(problem_values[i])
        return answer
    elif problem_values[-1] == "+":
        answer = 0
        for i in range(len(problem_values)-1):
            answer = answer+int(problem_values[i])
        return answer

def cephalapod_tabulate(problem_values):
    num_digits = len(max(problem_values, key=len))
    if problem_values[-1] == "*":
        answer = 1
        for i in range(num_digits-1, -1, -1):
            written_value = ''
            for j in range(len(problem_values)-1):
                written_value += problem_values[j][i]
            answer = answer*int(written_value)
        return answer
    elif problem_values[-1] == "+":
        answer = 0
        for i in range(num_digits-1, -1, -1):
            written_value = ''
            for j in range(len(problem_values)-1):
                written_value += problem_values[j][i]
            answer = answer+int(written_value)
        return answer

#%% Perform calculations
part1_answers = []
part2_answers = []
for problem in problem_inputs:
    part1_answers.append(human_tabulate(problem))
    part2_answers.append(cephalapod_tabulate(problem))

part1_sol = sum([int(x) for x in part1_answers])
print("Part 1 Answer is: "+str(part1_sol))
    
part2_sol = sum([int(x) for x in part2_answers])
print("Part 2 Answer is: "+str(part2_sol))



