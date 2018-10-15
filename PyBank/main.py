import os
import csv

csvpath = os.path.join('budget_data.csv')


with open(csvpath, newline= '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ',')

    #Count Months
    csvfile.seek(0)
    month_count = sum(1 for row in csvreader) - 1
    #Sum of Monthly Profit
    csvfile.seek(0)
    next(csvreader)
    moneytotal = sum(int(row[1]) for row in csvreader)
    
    #Max Monthly Profit
    csvfile.seek(0)
    
    next(csvreader)
    maxvalue = max(int(row[1]) for row in csvreader)
    
    csvfile.seek(0)
    next(csvreader)
    
    for row in csvreader:
        if int(row[1]) == maxvalue:
            maxvaluedate = str(row[0])
    
    #Min Monthly Profit
    csvfile.seek(0)
    next(csvreader)
    
    minvalue = min(int(row[1]) for row in csvreader)

    csvfile.seek(0)
    next(csvreader)

    for row in csvreader:

        if int(row[1]) == minvalue:
            minvaluedate = str(row[0])


    print("Financial Analysis")
    print("--------------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${moneytotal}")
    print(f"Greatest Increase in Profits: {maxvaluedate} (${maxvalue})")
    print(f"Greatest Decrease in Profits: {minvaluedate} (${minvalue})")

    textreportname = 'Financial-Analysis.txt'

    myfile = open(textreportname, 'w')

    myfile.write("Financial Analysis\n")
    myfile.write("--------------------------\n")
    myfile.write(f"Total Months: {month_count}\n")
    myfile.write(f"Total: ${moneytotal}\n")
    myfile.write(f"Greatest Increase in Profits: {maxvaluedate} (${maxvalue})\n")
    myfile.write(f"Greatest Decrease in Profits: {minvaluedate} (${minvalue})\n")

    