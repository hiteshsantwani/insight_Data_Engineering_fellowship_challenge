# This module is used for validating the output from pharmacy_counting.py with output from pandas

# Load the Pandas libraries with alias 'pd'

import pandas as pd

input_file_df = pd.read_csv("/Users/hiteshsantwani/Desktop/"
                         "Insight Fellowship Coding challenge/MySolution2/insight_Data_Engineering_fellowship_challenge/"
                         "insight_testsuite/tests/test_1/input/input_pandas")

mapping = {
    'id': 'id',
    'prescriber_last_name': 'name',
           'prescriber_first_name': 'name',
           'drug_name' : 'drug_name',
           'drug_cost' : 'drug_cost'}

print(input_file_df.head())

input_file_df = input_file_df.set_index('id').groupby(mapping, axis=1).sum()
input_file_df.name = input_file_df.groupby('drug_name').name.count()
input_file_df.drug_cost = input_file_df.groupby('drug_name').drug_cost.sum()
