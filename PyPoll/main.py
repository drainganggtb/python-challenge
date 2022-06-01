#Dependencies
import os
import csv

#here is our file
election_csv = os.path.join("Resources", "election_data.csv")

#Begin by defining variables and initializing them
total_votes=0
winner=""
candidate_options = []
candidate_votes = []
Percents=[]


#Open csv and skip header 
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    csv_header = next(csv_file)

    #read through each row of data
    for row in csv_reader:
        #count number of rows which == number of votes
        total_votes+=1
        if row[2] in candidate_options:
            candidate_votes[candidate_options.index(row[2])]+=1
        else:
            candidate_options.append(row[2])
            candidate_votes.append(1)
    print(total_votes)
    # print(candidate_options)
#Assign percents
for votes in candidate_votes:
    #f is floating points, 3 specify 3 digits 
    Percents.append('%.3f'%((votes*100)/total_votes))
#find winner
winner=candidate_options[candidate_votes.index(max(candidate_votes))]

#print results
print("Election Results \n.........................")
print(f"Total Votes: {total_votes}\n.........................")
for i in range(len(candidate_options)):
    print(f"{candidate_options[i]}: {Percents[i]}% [{candidate_votes[i]}]")
print(".........................")
print(f"Winner: {winner}")
print(".........................")

#send to txt file
results=open("analysis/results.txt", "w")
results.write("Election Results \n.........................\n")
results.write(f"Total Votes: {total_votes}\n.........................\n")
for i in range(len(candidate_options)):
    results.write(f"{candidate_options[i]}: {Percents[i]}% [{candidate_votes[i]}]\n")
results.write(".........................\n")
results.write(f"Winner: {winner}\n")
results.write(".........................")
