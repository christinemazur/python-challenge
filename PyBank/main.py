# * In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# * Your task is to create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset
#   * The net total amount of "Profit/Losses" over the entire period
#   * The average of the changes in "Profit/Losses" over the entire period
#   * The greatest increase in profits (date and amount) over the entire period
#   * The greatest decrease in losses (date and amount) over the entire period

#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.
import os
import csv

# read csv file, count the number of non-header rows and then put values in 2 lists
Months = 0
Profits = []
Dates = []

with open("../Resources/budget_data.csv", newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    for row in csvreader:
        Months += 1
        Dates.append(row[0])
        Profits.append(int(row[1]))

TotalProfits = Profits[0]  #put the first mo profit into total profit)
TotaledChanges = 0
BiggestInc = 0
BiggestDec = 0
BiggestIncDate = 0
BiggestDecDate = 0
CurrentChange = 0

#Start at 1 rather than 0 so we can calculate the change in profit below
for n in range (1, Months):
    #Add current mo. to total profits
    TotalProfits += Profits[n]
    
    #Calculate the change between this month and the month before it and then add it to the totaled changes
    CurrentChange = Profits[n] - Profits[n-1]
    TotaledChanges += CurrentChange
    
#Check if the current change was the biggest change and if so, make it the biggest increase or decrease amount and date
    if CurrentChange > BiggestInc:
        BiggestInc = CurrentChange
        BiggestIncDate = Dates[n]
    elif CurrentChange < BiggestDec:
        BiggestDec = CurrentChange
        BiggestDecDate = Dates[n]

#Print to screen
print("Financial Analysis")
print("----------------------------")
print(f"Months: {Months}")
print(f"Total Profits: ${(TotalProfits):.2f}")
print(f"Average Change: ${(TotaledChanges/(Months - 1)):.2f}")
print(f"Greatest Increase in Profits: {BiggestIncDate} (${(BiggestInc):.2f})")
print(f"Greatest Decrease in Profits: {BiggestDecDate} (${(BiggestDec):.2f})")

#print output results to txt file
with open("Financial Analysis.txt","w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Months: {Months}\n")
    txtfile.write(f"Total Profits: ${(TotalProfits):.2f}\n")
    txtfile.write(f"Average Change: ${(TotaledChanges/(Months - 1)):.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {BiggestIncDate} (${(BiggestInc):.2f})\n")
    txtfile.write(f"Greatest Decrease in Profits: {BiggestDecDate} (${(BiggestDec):.2f})\n")