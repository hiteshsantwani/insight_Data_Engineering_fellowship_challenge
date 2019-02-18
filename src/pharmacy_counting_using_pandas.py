# This module is used for validating the output from pharmacy_counting.py with output from pandas
# Load the Pandas libraries with alias 'pd'

import pandas as pd
import numpy as np
import unittest

import os
import sys
sys.path.insert(0, os.path.basename(__file__))

"""

function to generate the solution using pandas

Parameters
----------
input_file_df : location of the input file

Returns
-------
DataFrame conating the results

"""
def solutionUsingPandas(input_file_path):

    mapping = {
        'id': 'id',
        'prescriber_last_name': 'name',
        'prescriber_first_name': 'name',
        'drug_name': 'drug_name',
        'drug_cost': 'drug_cost'}

    input_file_df = pd.read_csv(input_file_path)
    input_file_df = input_file_df.set_index('id').groupby(mapping, axis=1).sum()
    input_file_df_drug_cost = input_file_df.groupby('drug_name')['drug_cost'].agg([np.sum])
    input_file_df_drug_cost['name'] = input_file_df.groupby('drug_name').name.unique()
    input_file_df_drug_cost['num_prescriber'] = input_file_df_drug_cost["name"].apply(lambda x: len(x))
    input_file_df = input_file_df_drug_cost.drop(columns=['name']).reset_index().rename(columns={'sum': 'total_cost'})
    input_file_df = input_file_df[['drug_name', 'num_prescriber', 'total_cost']]

    return input_file_df