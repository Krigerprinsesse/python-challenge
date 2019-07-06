import os
import csv

elec_csv = (r"C:\Users\grace\python-challenge\PyPoll\election_data.csv")

total_votes = []
votes_index = 0
county_index = 1
candidate_index = 2
candidates_list = []
candidates_dict = {}

with open(elec_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        total_votes.append(row[0])

        if row[2] not in candidates_list:
            candidates_list.append(row[2])
            candidates_dict.update({row[2]:0})
        candidates_dict[row[2]] = candidates_dict[row[2]] + 1
print("Election Results")
print("-----------------")
print(f"Total Votes: {len(total_votes)}")
print(f"Candidates: {candidates_list}")
print(candidates_dict)

output_path = (r"C:\Users\grace\python-challenge\Pypoll\results.txt")

with open (output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-----------------\n")
    file.write(f"Total Votes: {len(total_votes)}\n")
    file.write(f"Candidates: {candidates_list}\n")
    file.write(f"List{candidates_dict}\n")