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
import sys
import time
from src.pharmacy_counting_implementation import process_input_file, create_output, peek


# It takes one minute to process 24 million records

inputfile, outputfile = sys.argv[1:]

#inputfile = "/Users/hiteshsantwani/Desktop/Insight Fellowship Coding challenge/Submission/insight_Data_Engineering_fellowship_challenge/input/de_cc_data.txt"
#outputfile = "/Users/hiteshsantwani/Desktop/Insight Fellowship Coding challenge/Submission/insight_Data_Engineering_fellowship_challenge/output/top_drug_cost_test"

print("Start")
start = time.time()
print('Total Lines Processed', process_input_file(inputfile))
end = time.time()

print('It took: ', end - start, 'Seconds')
create_output(outputfile)

peek(outputfile)