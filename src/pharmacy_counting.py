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
import time

sys.path.insert(0, os.path.basename(__file__))

##############################
# Global Constants
ENCODING = 'utf8'

ZERO = 0
ONE = 1
Two = 2
Three = 3

names_dictionary = dict(set())
cost_dictionary = dict()
##############################

##############################
# Unit testable methods

"""

function to show head of output

"""
def peek():
    # Open and print top 10 lines of the output file
    with open(outputfile, 'rb') as output:
        record = output.readline()
        lineCount = ZERO
        while len(record) > ZERO and lineCount < 10:
            lineCount += ONE
            print(record.decode(ENCODING))
            record = output.readline()


"""

function to remove extra ','

Parameters
----------
record : a single record from input file

Returns
-------
record
    a record with no extra ','

"""
def handle_misaligned_record(record):

    if record.find('"') >= ZERO:
        start = record.find('"')

        while start >= ZERO:
            end = record[start + ONE:].find('"')
            if end >= ZERO:
                end = end + start + ONE
                record = record[:start] + record[start:end + ONE].replace(',', '') + record[end + ONE:]
            start = record[end + ONE:].find('"')

    return record

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

    lines_count = ZERO

    with open(input_file_Name, 'rb') as input:

        input.__next__()
        entry = input.readline()

        while len(entry) > ZERO:

            entry = entry.decode('%s' % ENCODING)
            lines_count += ONE

            entry = handle_misaligned_record(entry)

            entry = entry.split(',')
            doctor_name = ' '.join(entry[ONE:Three])

            try:
                names_dictionary[entry[Three]].add(doctor_name)
                cost_dictionary[entry[Three]] += float(entry[-ONE])
            except KeyError:
                names_dictionary[entry[Three]] = {doctor_name}
                cost_dictionary[entry[Three]] = float(entry[-ONE])

            if lines_count % 10**6 == ZERO:
                print('Lines Processed:', lines_count//10**6, 'million' )

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

        for drug, value in sorted(cost_dictionary.items(), key=lambda x: (x[1], x[0]), reverse=True):
            next_line = ','.join([drug, str(len(names_dictionary[drug])), str(round(cost_dictionary[drug], Two))])
            next_line += '\n'
            output.write(bytes(next_line, ENCODING))

        output.close()

################################

# It takes one minute to process 24 million records

inputfile, outputfile = sys.argv[1:]

#inputfile = "/Users/hiteshsantwani/Desktop/Insight Fellowship Coding challenge/Submission/insight_Data_Engineering_fellowship_challenge/input/itcont.txt"
#outputfile = "/Users/hiteshsantwani/Desktop/Insight Fellowship Coding challenge/Submission/insight_Data_Engineering_fellowship_challenge/output/top_drug_cost_test"

print("Start")
start = time.time()
print('Total Lines Processed', process_input_file(inputfile))
end = time.time()

print('It took: ', end - start, 'Seconds')
create_output(outputfile)

peek()