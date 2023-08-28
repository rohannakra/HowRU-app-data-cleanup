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
WPA_morning_testing_df = pd.read_csv('../clean data/WPA_morning_testing.csv')
WPA_night_training_df = pd.read_csv('../clean data/WPA_night_training.csv')


# Inspect Columns.
morning_tests = WPA_morning_testing_df.loc[:, 'wpa_morning_testing']

night_tests = WPA_night_training_df.loc[:, 'wpa_night_testing']
night_training_pairs = WPA_night_training_df.loc[:, 'wpa_training']    # No need to mess with this


# Make New DataFrame for Testing.
def word_pairs_df(initial_df, subjects: int):
    np_array = []
    columns = []

    for sample_index in range(subjects):

        # Put into readable json format before conversion.
        word_pairs_str = initial_df[sample_index].replace("'", '"')
        word_pairs_str = word_pairs_str.replace('True', 'true')
        word_pairs_str = word_pairs_str.replace('False', 'false')
        
        # Convert using json.
        word_pairs_list = json.loads(word_pairs_str)
        
        for i in range(len(word_pairs_list)):
            if sample_index == 0:
                columns_default = list(word_pairs_list[i].keys())
                for column in columns_default:
                    columns.append(f'{column}_{i+1}')
        
        sample_values = []    # This variable is for the individual word pairs

        for word_pair_dict in word_pairs_list:
            sample_values.append(list(word_pair_dict.values()))
            
        np_array.append(sample_values)
        
    np_array = np.array(np_array, dtype='O')
    np_array = np_array.reshape(np_array.shape[0], -1)

    dataframe = pd.DataFrame(np_array, columns=columns)
    return dataframe

morning_tests_df = word_pairs_df(morning_tests, 7)
night_tests_df = word_pairs_df(night_tests, 8)


# Add Columns to CSV.
for column in list(morning_tests_df.columns):
    WPA_morning_testing_df[column] = morning_tests_df[column]

for column in list(night_tests_df.columns):
    WPA_night_training_df[column] = night_tests_df[column]


# Get rid of Previous Columns.
WPA_morning_testing_df.drop(columns=['wpa_morning_testing'], inplace=True)
WPA_night_training_df.drop(columns=['wpa_night_testing'], inplace=True)


# Export to New CSV.
WPA_morning_testing_df.to_csv('../clean data/WPA updated/WPA_morning_testing_updated.csv')
WPA_night_training_df.to_csv('../clean data/WPA updated/WPA_night_training_updated.csv')
