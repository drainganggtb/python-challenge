#Dependencies
import os
import csv

#here is our file
election_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

#Begin by defining variables and initializing them
total_votes=0
winner=""
candidate_options = []
candidate_votes = {}
winning_count=0


#Open csv and skip header 
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    csv_header = next(csv_file)

    #read through each row of data
    for row in csv_reader:
        #count number of rows which == number of votes
        total_votes+=1
