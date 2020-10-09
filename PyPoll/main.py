#Dependencies
import os
import csv

#here is our file
election_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

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

    #     #candidate name 
    #     candidate_name = row[2]

    #     #conditional to populate array of candidate options
    #     if candidate_name not in candidate_options:
    #         candidate_options.append(candidate_name)

    #         #begin tracking voter counts per candidate
    #         candidate_votes[candidate_name]=0
            
    #         #add vote to candidate's count
    #         candidate_votes[candidate_name]+=1  
    # print(total_votes)
