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


# Get data
dataset = pd.read_csv("../original data/HowRU_app_data_tasks_and_questionnaire_summer_only.csv")

# Choose only the columns you need:
data = dataset.loc[:, ["id", "user_id", "user", "data"]]


# Data Cleanup
def cleanup(filename, task_string):
    np_array = []
    columns = []

    # Set columns to max amount.
    for sample_index in range(len(data['data'])):

        sample_data = data['data'][sample_index]

        if type(task_string) == list:
            if all([task_s in sample_data for task_s in task_string]):
                sample_data_dict = json.loads(sample_data)

                data_columns = list(column for column in sample_data_dict['data'])
                metadata_columns = ['started_at', 'finished_at']

                columns_test = ['id', 'user_id', 'user', *data_columns, *metadata_columns]

                if len(columns_test) > len(columns):
                    columns = columns_test
        else:
            if task_string in sample_data:
                sample_data_dict = json.loads(sample_data)
            
                data_columns = list(column for column in sample_data_dict['data'])
                metadata_columns = ['started_at', 'finished_at']

                columns_test = ['id', 'user_id', 'user', *data_columns, *metadata_columns]

                if len(columns_test) > len(columns):
                    columns = columns_test

    # Add to np_array (based on parameters)
    for sample_index in range(len(data['data'])):
        sample_id = data['id'][sample_index]
        sample_user_id = data['user_id'][sample_index]
        sample_user = data['user'][sample_index]
        sample_data = data['data'][sample_index]

        # Expand data column.
        sample_data_dict = json.loads(sample_data)

        # Data & metadata values.
        data_values = []

        for column in columns[3:-2]:
            try:
                value = sample_data_dict['data'][column]
            except KeyError:
                value = 'N/A'
            data_values.append(str(value))

        metadata_values = list(value for value in sample_data_dict['metadata'].values())[-2:]   

        # Recreate sample_data
        sample_data_new = [*data_values, *metadata_values]

        if type(task_string) == list:
            if all([task_s in sample_data for task_s in task_string]):
                np_array.append([sample_id, sample_user_id, sample_user, *sample_data_new])
        else:
            if task_string in sample_data:
                np_array.append([sample_id, sample_user_id, sample_user, *sample_data_new])
    
    # Convert to dataframe.
    dataframe = pd.DataFrame(np.array(np_array), columns=columns)

    # Convert to csv.
    dataframe.to_csv(f'../clean data/{filename}.csv')


# Cleanup tasks.
cleanup('sleep_diary_morning', 'where_EMA_morning')
cleanup('finger_tapping_night_testing', ['Night Testing', 'finger_tap'])
cleanup('finger_tapping_night_training', ['Night Training', 'finger_tap'])
cleanup('finger_tapping_morning_testing', ['Morning Testing', 'finger_tap'])
cleanup('WPA_morning_training', ['wpa_training', "Night Training"])
cleanup('sleep_diary_evening', 'where_EMA_evening')
cleanup('sleep_diary_forget_night', 'caffeinated_beverages')
cleanup('sleep_diary_forget_morning', 'get_out_of_bed')
cleanup('VGE_questionnaire', 'regularly_plays_games')
cleanup('PSAM_questionnaire', 'sure_parent')
cleanup('FSS_questionnaire', 'household_income')
cleanup('APQ_parent_questionnaire', 'talk_child')
cleanup('PSS_questionnaire', 'upset_something_unexpected')
cleanup('GAD-7_questionnaire', 'nervous_anxious_onedge')
cleanup('CASSS_questionnaire', 'parent_proud')
cleanup('CES-D_questionnaire', 'more_bother')
cleanup('IPPA_questionnaire', 'respect_feeling')
cleanup('PDS_questionnaire', 'height_growth')
