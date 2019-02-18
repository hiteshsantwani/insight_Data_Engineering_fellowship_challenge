# Load the Pandas libraries with alias 'pd'

import unittest
from src.pharmacy_counting import process_input_file, create_output


input_file_Name = '/Users/hiteshsantwani/Desktop/Insight Fellowship Coding challenge/MySolution2/insight_Data_Engineering_fellowship_challenge/input/de_cc_data.txt'
input_file_Name_pandas = '/Users/hiteshsantwani/Desktop/Insight Fellowship Coding challenge/MySolution2/insight_Data_Engineering_fellowship_challenge/insight_testsuite/tests/test_1/input/input_pandas'
output_file_Name = '/Users/hiteshsantwani/Desktop/Insight Fellowship Coding challenge/MySolution2/insight_Data_Engineering_fellowship_challenge/output/top_cost_drug.txt'

# start dumping file to output location
create_output(output_file_Name)
print("number of lines processed: ", process_input_file(input_file_Name_pandas))

class test_my_solution(unittest.TestCase):

    process_input_file()
    create_output()

    pass
