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
Three = 3
ONE = 1

input_file_Name = '/Users/hiteshsantwani/Desktop/Insight Fellowship Coding challenge/MySolution2/insight_Data_Engineering_fellowship_challenge/input/de_cc_data.txt'
output_file_Name = '/Users/hiteshsantwani/Desktop/Insight Fellowship Coding challenge/MySolution2/insight_Data_Engineering_fellowship_challenge/output/top_cost_drug.txt'


names_dictionary = dict(set())
cost_dictionary = dict()


def process_input_file():

    lines_count = 0

    with open(input_file_Name, 'rb') as input:

        input.__next__()
        entry = input.readline()

        while len(entry) > 0:

            entry = entry.decode('utf8')
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


def create_output():
    with open(output_file_Name, 'wb') as output:
        output.write(b'drug_name,num_prescriber,total_cost\n')

        for drug in cost_dictionary.keys():
            next_line = ','.join([drug, str(len(names_dictionary[drug])), str(cost_dictionary[drug])])
            next_line += '\n'
            output.write(bytes(next_line, 'utf8'))



print("number of lines processed: ", process_input_file())

# start dumping file to output location
create_output()



# It takes one minute to process 24 million records