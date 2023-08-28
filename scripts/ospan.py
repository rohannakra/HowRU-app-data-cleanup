# Imports.
import numpy as np
import pandas as pd
from scipy import stats
from scipy.spatial import distance
from matplotlib import pyplot as plt
from itertools import permutations
import glob
import csv
import os
import re
import json


# Get Data.
with open('../original data/OSPAN data/Newest_OSPAN1.txt', 'r') as OSPAN1:
    OSPAN1 = OSPAN1.read()
    OSPAN1 = OSPAN1.replace("'", '"')
    OSPAN1 = OSPAN1.replace('True', 'true')
    OSPAN1 = OSPAN1.replace('False', 'false')

    ospan_1 = json.loads(OSPAN1)


# Make New DataFrame for Testing.
def ospan_data_df(initial_data, filename):
    np_array = []
    columns = []

    # Sort each OSPAN.
    initial_data['ospan_1'] = sorted(initial_data['ospan_1'], key=len)
    initial_data['ospan_2'] = sorted(initial_data['ospan_2'], key=len)
    initial_data['ospan_3'] = sorted(initial_data['ospan_3'], key=len)

    # Add values + columns.

    # OSPAN.
    for problem_set_i in range(1, 4):
        problem_set = initial_data[f'ospan_{problem_set_i}']
        values = []

        # Letter set.
        for letter_set_i in range(4):
            letter_set = problem_set[letter_set_i]

            # Problem.
            for problem_i in range(len(letter_set)):
                problem = letter_set[problem_i]

                if problem_i == len(letter_set) - 1:    # At this point, at the end of the letter set... this is where we're given the full letter set.
                    user_letters = problem['input']
                    letters = problem['letters']
                    user_input_time = problem['inputTime']
                    user_start_time = problem['startTime']

                    # Add values.
                    values.extend([user_letters, letters, user_input_time, user_start_time])
                    if problem_set_i == 1:    # Only add columns if this is the first problem set.
                        columns.extend(['user_letters', 'letters', 'user_input_time', 'user_start_time'])
                
                else:
                    equation_old = problem['equation']
                    
                    equation_new = f"{equation_old['a']} {equation_old['operator']} {equation_old['b']} = {equation_old['result']}"
                    letter = problem['letter']
                    user_is_correct = problem['correctAnswer']
                    if problem['missed'] == True:
                        choice = 'missed'
                    else:
                        choice = problem['choice']

                    # Add values.
                    values.extend([equation_new, letter, user_is_correct, choice])
                    if problem_set_i == 1:
                        columns.extend(['equation', 'letter', 'user_is_correct', 'choice'])

        # Add values to np_array.          
        np_array.append(values)
    
    # Finalize data.
    np_array = np.array(np_array, dtype='O')
    dataframe = pd.DataFrame(np_array, columns=columns)

    # Create new index.
    index = ['OSPAN 1', 'OSPAN 2', 'OSPAN 3']
    dataframe['index'] = index
    dataframe.set_index('index', inplace=True)

    dataframe.to_csv(f'../clean data/OSPAN updated/{filename}.csv')


ospan_data_df(ospan_1['data'], '101_OSPAN_1')
