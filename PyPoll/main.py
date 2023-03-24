# Import the os module and CSV module
import os
import csv

# Module for reading CSV files
csvpath = os.path.join('Resources', 'election_data.csv')

#Declaring variables and dictionary
total_rec=0
candidate_vote = {}

#Reading CSV file and checking for count
with open(csvpath,'r') as csvhandler:
    
    csvreader = csv.reader(csvhandler,delimiter=",")
    csv_header = next(csvreader)    #Getting headers

    for row in csvreader:
        total_rec=total_rec+1
        if row[2] not in candidate_vote:
            candidate_vote[row[2]]=1
        else:
            candidate_vote[row[2]]+=1

#Calculate winner with max votes
winner = max(candidate_vote,key=candidate_vote.get)

#Print results
print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {total_rec}")
print("-------------------------------------")
for key,value in candidate_vote.items():
    print(f"{key}: {round(((value/total_rec)*100),3)}% ({value})")
print("-------------------------------------")
print(f"Winner: {winner}")
print("-------------------------------------")

#Writing all data to text file
output_file = os.path.join('Analysis', 'PyBank_Output.txt')

with open(output_file, 'w') as writer_handle:
    print("Financial Analysis",file=writer_handle)
    print("Election Results",file=writer_handle)
    print("-------------------------------------",file=writer_handle)
    print(f"Total Votes: {total_rec}",file=writer_handle)
    print("-------------------------------------",file=writer_handle)
    for key,value in candidate_vote.items():
        print(f"{key}: {round(((value/total_rec)*100),3)}% ({value})",file=writer_handle)
    print("-------------------------------------",file=writer_handle)
    print(f"Winner: {winner}",file=writer_handle)
    print("-------------------------------------",file=writer_handle)
