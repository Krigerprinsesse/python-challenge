import os
import csv
import numpy as np

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
    print("--------------------------")
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {len(total_votes)}")

    for name,nvotes in candidates_dict.items():
        print (f"{name}:  ({nvotes})  %{nvotes/len(total_votes)*100}")
    print("---------------------------")
    print(f"Winner! {candidates_list[np.argmax(candidates_dict)]}")
    print("---------------------------")



output_path = (r"C:\Users\grace\python-challenge\Pypoll\results.txt")

with open (output_path, 'w') as file:
    file.write("---------------------------\n")
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f"Total Votes: {len(total_votes)}\n")
    for name,nvotes in candidates_dict.items():
        file.write(f"{name} Votes: ({nvotes})  %{nvotes/len(total_votes)*100}\n")
    file.write("---------------------------\n")
    file.write(f"Winner! {candidates_list[np.argmax(candidates_dict)]}\n")
    file.write("---------------------------")