import os
import pandas as pd

filepath = "election_data.csv"

election_df = pd.read_csv(filepath)

election_df.head()




#Make data frame and count candidates
votes_df = pd.DataFrame(election_df['Candidate'].value_counts())
votes_df = votes_df.sort_values('Candidate', ascending=False)
candidate_count = len(votes_df['Candidate'])
totalvotes = votes_df['Candidate'].sum()
winner = votes_df.index[0]

print("Financial Analysis")
print("--------------------------------")

print(f"Total Votes: {totalvotes}")
print("--------------------------------")


for x in range(0, candidate_count):
    
    print(f"{votes_df.index[x]}: {votes_df.iloc[x,0]}")
    
print("--------------------------------")
print(f"Winner: {winner}")
print("--------------------------------")
    
outputname = "election-results.txt"

myfile = open(outputname, 'w')

myfile.write("Financial Analysis\n")
myfile.write("--------------------------------\n")

myfile.write(f"Total Votes: {totalvotes}\n")
myfile.write("--------------------------------\n")


for x in range(0, candidate_count):
    
    myfile.write(f"{votes_df.index[x]}: {votes_df.iloc[x,0]}\n")
    
myfile.write("--------------------------------\n")
myfile.write(f"Winner: {winner}\n")
myfile.write("--------------------------------\n")
    