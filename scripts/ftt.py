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
with open('../original data/FTT data/Finger Tapping Test Formatted.txt', 'r') as FTT_ex_subject_data:
    FTT_ex_subject_data = FTT_ex_subject_data.read()
    FTT_ex_subject_data = FTT_ex_subject_data.replace("'", '"')
    FTT_ex_subject_data = FTT_ex_subject_data.replace('True', 'true')
    FTT_ex_subject_data = FTT_ex_subject_data.replace('False', 'false')

    ftt_ex_subject = json.loads(FTT_ex_subject_data)

    
# Make New DataFrame for Testing.
def ftt_data_df(initial_data, filename, SID):
    np_array = []
    columns = ['SID', 'test_type/trial', 'target_value', 'user_input', 'time', 'start_time']

    SID = SID

    for trial in range(len(initial_data['finger_tap'])):
        target = initial_data['finger_tap'][trial]['target']
        start_time = initial_data['finger_tap'][trial]['startTime']

        for i in range(len(initial_data['finger_tap'][trial]['strokes'])):
            input_digit = initial_data['finger_tap'][trial]['input'][i]
            time = initial_data['finger_tap'][trial]['strokes'][i]

            row = [SID, f'Night Training/{trial+1}', target, input_digit, time, start_time]
    
            np_array.append(row)

    np_array = np.array(np_array, dtype='O')
    dataframe = pd.DataFrame(np_array, columns=columns)

    dataframe.to_csv(f'../clean data/FTT updated/{filename}.csv')


ftt_data_df(ftt_ex_subject['data'], '102_FTT_night_training', '102')
