import os
import csv
import numpy as np


budget_csv = (r"C:\Users\grace\python-challenge\Pybank\budget_data.csv")
    
count = 0
net_total = 0
row_index_net = 1
total_months = []
last_month_p = 0
month_over_month = []

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        

        total_months.append(row[0])

        float_net = float(row[row_index_net])
        net_total += float_net

        
    
        if count > 0:
            month_over_month.append(float_net - last_month_p)
        count +=1
        last_month_p = float_net
        


ave_dif = (sum(month_over_month)/(len(month_over_month)))

print ("Financial Analysis")
print("-------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: $ {net_total}")
print(f"Average Change $ {ave_dif}")
print (f"Greatest Increase in Profits: $ {max(month_over_month)}")
print (f"Greatest Decrease in Profits: $ {min(month_over_month)}")


output_path = (r"C:\Users\grace\python-challenge\Pybank\analysis.txt")

with open (output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write(f"Total Months: {len(total_months)}\n")
    file.write(f"Total: $ {net_total}\n")
    file.write(f"Average Change $ {ave_dif}\n")
    file.write(f"Greatest Increase in Profits: $ {max(month_over_month)}\n")
    file.write(f"Greatest Decrease in Profits: $ {min(month_over_month)}\n")