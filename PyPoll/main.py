import os
import csv

csvpath = os.path.join("election_data.csv")

with open(csvpath, newline= '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    next(csvreader)

    totalvotes = sum(1 for row in csvreader)

    csvfile.seek(0)
    next(csvreader)

    khanvotes = sum(1 for row in csvreader if row[2] == "Khan")

    csvfile.seek(0)
    next(csvreader)

    correyvotes = sum(1 for row in csvreader if row[2] == "Correy")

    csvfile.seek(0)
    next(csvreader)

    livotes = sum(1 for row in csvreader if row[2] == "Li")

    csvfile.seek(0)
    next(csvreader)

    tooleyvotes = sum(1 for row in csvreader if row[2] == "O'Tooley")

    khanpercentage = str(round((int(khanvotes) / int(totalvotes)) * 100, 4))
    correypercentage = str(round((int(correyvotes) / int(totalvotes)) * 100, 3))
    lipercentage = str(round((int(livotes) / int(totalvotes)) * 100, 5))
    tooleypercentage = str(round((int(tooleyvotes) / int(totalvotes)) * 100, 5))




    winner = max(khanvotes, correyvotes, livotes, tooleyvotes)

    if winner == khanvotes:
        winnername = "Khan"
    
    elif winner == correyvotes:
        winnername = "Correy"
    
    elif winner == livotes:
        winnername = "Li"
    
    elif winner == tooleyvotes:
        winnername = "O'Tooley"
    
    
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {totalvotes}")
    print("----------------------------")
    print(f"Khan: {khanpercentage}% ({khanvotes})")
    print(f"Correy: {correypercentage}% ({correyvotes})")
    print(f"Li: {lipercentage}% ({livotes})")
    print(f"O'Tooley: {tooleypercentage}% ({tooleyvotes})")
    print("----------------------------")
    print(f"Winner: {winnername}")
    print("----------------------------")


    resultsname = "Election Results.txt"

    myfile = open(resultsname, 'w')

    myfile.write("Election Results\n")
    myfile.write("----------------------------\n")
    myfile.write(f"Total Votes: {totalvotes}\n")
    myfile.write("----------------------------\n")
    myfile.write(f"Khan: {str(khanpercentage)}% ({khanvotes})\n")
    myfile.write(f"Correy: {str(correypercentage)}% ({correyvotes})\n")
    myfile.write(f"Li: {lipercentage}% ({livotes})\n")
    myfile.write(f"O'Tooley: {tooleypercentage}% ({tooleyvotes})\n")
    myfile.write("----------------------------\n")
    myfile.write(f"Winner: {winnername}\n")
    myfile.write("----------------------------\n")
    