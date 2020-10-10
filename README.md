# python-challenge
The following projects **PyBank** and **PyPoll** involved gathering data from csv files through writing Python scripts. 
Within the folders for each challenge within this repository, the *main.py* file contains the necessary script to read through the csv files contained within the Resources folders.
Additionally, the **analysis** folder contains the file *results.txt*, which outputs the same information that the script prints in the terminal.

#PyBank
![alt text](http://www.korvia.com/wp-content/uploads/2018/02/Banking-Featured-Image.png)
-  In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
-  Your task is to create a Python script that analyzes the records to calculate each of the following:


    -  The total number of months included in the dataset


    -  The net total amount of "Profit/Losses" over the entire period


    -  The average of the changes in "Profit/Losses" over the entire period


    -  The greatest increase in profits (date and amount) over the entire period


    -  The greatest decrease in losses (date and amount) over the entire period

-  Here is what the output looks like, as seen in the PyBank analysis folder
'''python
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)


