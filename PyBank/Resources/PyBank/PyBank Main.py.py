import os
import csv

fileLoad = os.path.join("budget_data.csv")
outputFile = os.path.join("BudgetAnalysis.txt")

#variables
totalMonths = 0
totalRevenue = 0
monthlyChanges = []
months = []

with open(fileLoad) as budgetData:
    CSVreader = csv.reader(budgetData)
    
    header = next(CSVreader)
    firstRow = next(CSVreader)
    previousRevenue = float(firstRow[1])

    totalRevenue += float(firstRow[1])

    for row in CSVreader:
        totalMonths += 1

        totalRevenue += float(row[1])

        netChange = float(row[1]) - previousRevenue

        monthlyChanges.append(netChange)

        months.append(row[0])

        previousRevenue = float(row[1])

greatestIncrease = [months[0], monthlyChanges[0]]
greatestDecrease = [months[0], monthlyChanges [0]]

#calculate the average net change per month
averageChangesPerMonth = sum(monthlyChanges) / len(monthlyChanges)
    
#use loop to calculate the index of the greatest and least monthly change 
for m in range(len(monthlyChanges)):
    if(monthlyChanges[m] > greatestIncrease[1]):
        greatestIncrease[1] = monthlyChanges[m]
        greatestIncrease[0] = months[m]

    if(monthlyChanges[m] < greatestDecrease[1]):
        greatestDecrease[1] = monthlyChanges[m]
        greatestDecrease[0] = months[m]
output = (
f"Revenue Data Analysis \n"
f"---------------------- \n"
f"\tTotal Months = {totalMonths} \n"
f"\tTotal Revenue = ${totalRevenue:,.2f} \n"
f"\tAverage Changes Per Month = ${averageChangesPerMonth:,.2f} \n"
f"\tGreaest Increase In Profits ={greatestIncrease[0]} Amount ${greatestIncrease[1]:,.2f} \n"
f"\tGreaest Decrease In Profits ={greatestDecrease[0]} Amount ${greatestDecrease[1]:,.2f} \n"
)


print(output)

with open (outputFile, "w") as textfile:
    textfile.write(output)