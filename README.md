# Python Challenge
The following projects **PyBank** and **PyPoll** involved gathering data and outputting specific information from csv files through writing Python scripts. 
Within the folders in this repository, the *main.py* file contains the necessary script to analyze the csv files contained within the Resources folders.
Additionally, the **analysis** folder contains the file *results.txt*, which outputs the same information that the script prints in the terminal.

# PyBank
![alt text](http://www.korvia.com/wp-content/uploads/2018/02/Banking-Featured-Image.png)
-  In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
-  Your task is to create a Python script that analyzes the records to calculate each of the following:


    -  The total number of months included in the dataset


    -  The net total amount of "Profit/Losses" over the entire period


    -  The average of the changes in "Profit/Losses" over the entire period


    -  The greatest increase in profits (date and amount) over the entire period


    -  The greatest decrease in losses (date and amount) over the entire period

-  Here is what the output looks like, as seen in the PyBank analysis folder
```python
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
```
# PyPoll
![alt text](https://www.thephoenix.ie/wp-content/uploads/2020/01/3665-Polling-Station.jpg)

The idea behind this challenge is modernizing the voting process for a small town. 

-  You will be give a set of poll data called *election_data.csv*. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
    -  The total number of votes cast


    -  A complete list of candidates who received votes


    -  The percentage of votes each candidate won


    -  The total number of votes each candidate won


    -  The winner of the election based on popular vote.

-  The results which appear below are the result of the script. They can be found in *results.txt* within the analysis folder
```python
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
```


