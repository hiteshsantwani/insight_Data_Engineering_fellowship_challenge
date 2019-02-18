"""
If your input data, **`itcont.txt`**, is

id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
1000000001,Smith,James,AMBIEN,100
1000000002,Garcia,Maria,AMBIEN,200
1000000003,Johnson,James,CHLORPROMAZINE,1000
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
1000000005,Smith,David,BENZTROPINE MESYLATE,1500


then your output file, **`top_cost_drug.txt`**, would contain the following lines

drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,300

"""
import os
import sys
sys.path.insert(0, os.path.basename(__file__))

##############################
# Global Constants
ENCODING = 'utf8'
Three = 3
ONE = 1

names_dictionary = dict(set())
cost_dictionary = dict()
##############################

##############################
# Unit testable methods

"""

function to process input file and create the solution

Parameters
----------
input_file_df : location of the input file

Returns
-------
int
    number of lines processed
    
"""
def process_input_file(input_file_Name):

    lines_count = 0

    with open(input_file_Name, 'rb') as input:

        input.__next__()
        entry = input.readline()

        while len(entry) > 0:

            entry = entry.decode('%s' % ENCODING)
            lines_count += ONE

            entry = entry.split(',')
            doctor_name = ' '.join(entry[ONE:Three])

            try:
                names_dictionary[entry[Three]].add(doctor_name)
                cost_dictionary[entry[Three]] += float(entry[-ONE])
            except KeyError:
                names_dictionary[entry[Three]] = {doctor_name}
                cost_dictionary[entry[Three]] = float(entry[-ONE])

            entry = input.readline()
    return lines_count

"""

function to generate the solution using pandas

Parameters
----------
output_file_Name : location of the output file

"""

def create_output(output_file_Name):
    with open(output_file_Name, 'wb') as output:
        output.write(b'drug_name,num_prescriber,total_cost\n')

        for drug in sorted(cost_dictionary.keys()):
            next_line = ','.join([drug, str(len(names_dictionary[drug])), str(cost_dictionary[drug])])
            next_line += '\n'
            output.write(bytes(next_line, 'utf8'))

        output.close()

################################

# It takes one minute to process 24 million records
