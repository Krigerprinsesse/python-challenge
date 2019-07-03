import os
import csv

budget_csv = (r"C:\Users\grace\python-challenge\Pybank\budget_data.csv")
    
net_total = 0
row_index_net = 1
total_months = []
last_month_p = 0
month_over_month = []

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        float_net = float(row[row_index_net])
        net_total += float_net

    
        total_months.append(row[0])
        month_over_month.append(float_net - last_month_p)
        last_month_p = float_net


ave_dif = (sum(month_over_month)/(len(month_over_month)))

print ("Financial Analysis")
print("-------------------------")
print(f"Total Months: {len(month_over_month)}")
print(f"Total: $ {net_total}")
print(f"Average Change $ {ave_dif}")
print (f"Greatest Increase in Profits: $ {max(month_over_month)}")
print (f"Greatest Decrease in Profits: $ {min(month_over_month)}")