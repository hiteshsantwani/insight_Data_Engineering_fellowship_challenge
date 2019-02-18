# Load the Pandas libraries with alias 'pd'
from __future__ import with_statement
import unittest
from pathlib import Path
from src.pharmacy_counting_using_pandas import solutionUsingPandas
from src.pharmacy_counting import process_input_file, create_output

class validate_Op_with_Pandas(unittest.TestCase):

    def test_solutionUsingPandas(self):
        file = Path().absolute()
        path = str(file) + "/input/input_pandas"
        df = solutionUsingPandas(path)
        print(df.iloc[0, 0])
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


        with open(path) as f1:
            with open(op) as f2:
                if f1.read() == f2.read():
                    assert True
                    f1.close()
                    f2.close()
                else:
                    assert False
                    f1.close()
                    f2.close()

