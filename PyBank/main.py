#Dependencies
import os
import csv

#Specify file path
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#Initialize values for results
MonthCount=[]
Total=[]

#Open the file and specify variable to hold content
with open(budget_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    #skip header
    csv_header = next(csvfile)

    #read through rows of data after header (+= assignment operator -> c+=a == c=c+a)
    for rows in csv_reader:
        MonthCount.append(rows[0])
        
        #adds up numbers (defined as integers -> use string later in print) from Profit/Losses column starting after header(row1)
        Total.append(int(rows[1]))

    #now we need to find the average change in Profit/Losses
    change = []
    for x in range(1,len(Total)):
        change.append((int(Total[x])-int(Total[x-1])))
    
    #calculate average change
    change_average = sum(change)/len(change)

    #calculate total length of MonthCount variable
    total_months = len(MonthCount)

    # use python functions to calculate greatest increase and decrease in revenue
    greatest_increase = max(change)
    greatest_decrease = min(change)

    #finished gathering these data, now print results
    print("Financial Analysis")
    print("..................................................")
    print(f"Total Months: {total_months}")
    print("Total: " + "$" + str(sum(Total)))
    print("Average Change: " + "$" + str(change_average))
    print("Greatest Increase in Profits: " + str(MonthCount[change.index(max(change))+1]) + "(" + " $" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + str(MonthCount[change.index(min(change))+1]) + "(" + " $" + str(greatest_decrease) + ")")

    #nice! now write to a text file
    results=open("results.txt","w")
    results.write("Financial Analysis" + "\n")
    results.write("..................................."+ "\n")
    results.write(f"Total Months: {total_months}\n")
    results.write("Total: " + "$" + str(sum(Total))+ "\n")
    results.write("Average Change: " + "$" + str(change_average)+ "\n")
    results.write("Greatest Increase in Profits: " + str(MonthCount[change.index(max(change))+1]) + "(" + " $" + str(greatest_increase) + ")"+ "\n")
    results.write("Greatest Decrease in Profits: " + str(MonthCount[change.index(min(change))+1]) + "(" + " $" + str(greatest_decrease) + ")"+ "\n")




