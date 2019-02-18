# Load the Pandas libraries with alias 'pd'

import unittest
from pathlib import Path
from src.pharmacy_counting_using_pandas import solutionUsingPandas
from src.pharmacy_counting import process_input_file, create_output

class validate_Op_with_Pandas(unittest.TestCase):

    def test_solutionUsingPandas(self):
        file = Path().absolute()
        path = str(file) + "/input/input_pandas"
        df = solutionUsingPandas(path)

        assert df.iloc[0, 0] == "ABILIFY"

    def test_Comparison(self):
        file = Path().absolute()
        path = str(file) + "/input/input_pandas"
        df = solutionUsingPandas(path)
        outputpath = str(file) + "/output/output_pandas"
        df.to_csv(outputpath, index=None, header=True)

        process_input_file(path)
        op = str(file) + "/output/top_cost_drug_validation_test.txt"

        create_output(op)

        if open(path, 'r').read() == open(op, 'r').read():
            assert True


