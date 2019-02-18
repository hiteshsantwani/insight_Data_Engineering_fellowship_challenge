# Load the Pandas libraries with alias 'pd'

import unittest
from pathlib import Path
from src.pharmacy_counting import process_input_file, create_output, handle_misaligned_record


class test_my_solution(unittest.TestCase):

    def test_process_input_file(self):
        file = Path().absolute()
        path = str(file) + "/input/itcont.txt"

        lines_count = process_input_file(path)
        print(lines_count)
        assert lines_count != 0


    def test_create_output(self):
        file = Path().absolute()
        op = str(file) + "/output/top_cost_drug.txt"
        create_output(op)
        with open(op) as f1:
            if len(f1.readline()) != 0:
                assert True
                f1.close()
            else:
                assert False
                f1.close()

    def test_handle_misaligned_record(self):
        file = Path().absolute()
        path = str(file) + "/input/dirty_data"
        with open(path) as f1:
            record = f1.readline()
            record = handle_misaligned_record(record)
            assert record.count(',') == 4


