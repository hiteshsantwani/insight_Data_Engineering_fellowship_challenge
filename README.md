# insight_Data_Engineering_fellowship_challenge

# Problem
Imagine you are a data engineer working for an online pharmacy. You are asked to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name in ascending order.

Disclosure: The projects that Insight Data Engineering Fellows work on during the program are much more complicated and interesting than this coding challenge. This challenge only tests you on the basics.

This GitHub repository contains my solution to the coding challenge for the Fellows Program organized by Insight Data Science.

# Input Dataset

comma separated input file with 5 columns, e.g.,

```
id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
1000000001,Smith,James,AMBIEN,100
1000000002,Garcia,Maria,AMBIEN,200
1000000003,Johnson,James,CHLORPROMAZINE,1000
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
1000000005,Smith,David,BENZTROPINE MESYLATE,1500
```

The original dataset was obtained from the Centers for Medicare & Medicaid Services but has been cleaned and simplified to match the scope of the coding challenge. It provides information on prescription drugs prescribed by individual physicians and other health care providers. The dataset identifies prescribers by their ID, last name, and first name.  It also describes the specific prescriptions that were dispensed at their direction, listed by drug name and the cost of the medication. 

# Output 

My solution create the output file, `top_cost_drug.txt`, that contains comma (`,`) separated fields in each line.

Each line of this file should contain these fields:
* drug_name: the exact drug name as shown in the input dataset
* num_prescriber: the number of unique prescribers who prescribed the drug. For the purposes of this challenge, a prescriber is considered the same person if two lines share the same prescriber first and last names
* total_cost: total cost of the drug across all prescribers

For example

If your input data, **`itcont.txt`**, is
```
id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
1000000001,Smith,James,AMBIEN,100
1000000002,Garcia,Maria,AMBIEN,200
1000000003,Johnson,James,CHLORPROMAZINE,1000
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
1000000005,Smith,David,BENZTROPINE MESYLATE,1500
```

then your output file, **`top_cost_drug.txt`**, would contain the following lines
```
drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,300
```

## Repo directory structure

The directory structure for your repo should look like this:

├── README.md 
├── run.sh
├── src
│   └── pharmacy-counting.py
├── input
│   └── itcont.txt
├── output
|   └── top_cost_drug.txt
├── insight_testsuite
└── run_tests.sh
└── tests
└── test_1
|   ├── input
|   │   └── itcont.txt
|   |__ output
|   │   └── top_cost_drug.txt
├── your-own-test_1
├── input
│   └── your-own-input-for-itcont.txt
|── output
└── top_cost_drug.txt

