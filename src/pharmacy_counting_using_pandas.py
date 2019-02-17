# This module is used for validating the output from pharmacy_counting.py with output from pandas

# Load the Pandas libraries with alias 'pd'

import pandas as pd

input_file_df = pd.read_csv("/Users/hiteshsantwani/Desktop/"
                         "Insight Fellowship Coding challenge/MySolution2/insight_Data_Engineering_fellowship_challenge/"
                         "insight_testsuite/tests/test_1/input/input_pandas")

print(input_file_df.head())

print(input_file_df.groupby('drug_name').count())

