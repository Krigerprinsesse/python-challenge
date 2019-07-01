import os
import csv

budget_csv = (r"C:\Users\grace\python-challenge\Pybank\budget_data.csv")
    
net_total = 0
row_index_net = 2
            

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        float_net = float(row[row_index_net])
        net_total += float_net

        net_total
    


