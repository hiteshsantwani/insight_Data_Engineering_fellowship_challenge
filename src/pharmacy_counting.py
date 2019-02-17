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


input_file_Name = '/Users/hiteshsantwani/Desktop/Insight Fellowship Coding challenge/MySolution/input/itcont.txt'
output_file_Name = '/Users/hiteshsantwani/Desktop/Insight Fellowship Coding challenge/MySolution/output/top_cost_drug.txt'

#algo:

#read input file

# we need for each drug how many doctors prescribed it and how much is the total cost

# NO PANDAS!

# constraints algo sould scale up to millions of records

# can not use sorting because that would need loading of whole data in memory

# cannot use spark for parallelism

# Need to do it in O(n) time

# lets map each drug to the doctor that prescribed it using Dictionary and while doing so we can add the cost as well

lines_count = 0

names_dictionary = dict()
cost_dictionary = dict()

with open(input_file_Name, 'rb') as input:
    entry = input.readline()
    entry = input.readline()
    while len(entry) > 0:
        lines_count += 1

        entry = entry.split(',')
        doctor_name = ' '.join(entry[1:3])
        names_dictionary[entry[3]].add(doctor)
        cost_dictionary[entry[3]] += double(entry[-1])


