# Load the Pandas libraries with alias 'pd'

import unittest

from pathlib import Path

from src.pharmacy_counting_using_pandas import solutionUsingPandas


class validate_Op_with_Pandas(unittest.TestCase):

    def test_solutionUsingPandas(self):
        file = Path().absolute()
        path = str(file) + "/input/input_pandas"
        df = solutionUsingPandas(path)
        print(df.iloc[0, 0])
        assert df.iloc[0, 0] == "ABILIFY"

    def test_validation(self):
        file = Path().absolute()
        path = str(file) + "/input/input_pandas"
        df = solutionUsingPandas(path)
        outputpath = str(file) + "/output/output_pandas"
        df.to_csv(outputpath, index=None, header=True)




