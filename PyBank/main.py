
# Program: 
#   main.py
#
# Written by: 
#   Ricardo G. Mora, Jr  09/27/2021
#
# Description:
#   This progam reads data from CSV file "budget_data.csv" and calculates
#   the total number of months of financial data, the overall net profit
#   or loss, the month with the largest increase in profit from it's
#   previous month, the month with the largest decrease in profit from it's
#   previous month, and the average of the monthly changes in profit.
#   The results are placed into file "budget_summary.txt" and are also
#   displayed to the console.


import os
import csv

InputPath = os.path.join("Resources", "budget_data.csv")
OutputPath = os.path.join("Analysis", "budget_summary.txt")

# Open input file and read into csv reader:
with open(InputPath, "r", newline="") as ReadFile:
    DataReader = csv.reader(ReadFile, delimiter=",")
    
    # Skip header row:
    HeaderRow = next(DataReader)
    
    # Look at first row of data and initialize variables:
    FirstRow = next(DataReader)
    MonthCount = 1
    MaxMonthlyGain = 0
    MaxMonthlyLoss = 0
    MaxGainMonth = FirstRow[0]
    MaxLossMonth = FirstRow[0]
    FirstMonthProfit = int(FirstRow[1])
    ThisMonthProfit = int(FirstRow[1])
    PreviousMonthProfit = int(FirstRow[1])
    NetProfit = int(FirstRow[1])

    # Loop through remaining rows and increment MonthCount and NetProfit:
    for Row in DataReader:
        MonthCount = MonthCount + 1
        NetProfit = NetProfit + ThisMonthProfit
        
        # Calculate the ChangeInProfit between this month and the previous month:
        ThisMonthProfit = int(Row[1])
        ChangeInProfit = ThisMonthProfit - PreviousMonthProfit

        # If the ChangeInProfit is larger than MaxMonthlyGain, make it the new MaxMonthlyGain,
        # Else if the ChangeInProfit is smaller than  MaxMonthlyLoss, make it the new MaxMonthlyLoss:
        if ChangeInProfit > MaxMonthlyGain:
            MaxMonthlyGain = ChangeInProfit
            MaxGainMonth = Row[0]
        elif ChangeInProfit < MaxMonthlyLoss:
            MaxMonthlyLoss = ChangeInProfit
            MaxLossMonth = Row[0]
        PreviousMonthProfit = ThisMonthProfit

# Calculate the average of all changes in monthly profits using this simplification:
#   AvgChanges = ((Row2-Row1) + (Row3-Row2) + (Row4-Row3) + ... + (Row(n) - Row(n-1))) / (n-1)
#              = (Row2 - Row1 + Row3 - Row2 + Row4 - Row3 + ... + Row(n) - Row(n-1)) / (n-1)
#              = (Row2 - Row2 + Row3 - Row3 + Row4 - Row4 + ... + Row(n) - Row1) / (n-1)
#              = (Row(n) - Row1) / (n-1)
MeanMonthlyProfitChange = (ThisMonthProfit - FirstMonthProfit) / (MonthCount - 1)

# Output to terminal:
print("Financial Analysis")
print("------------------")
print(f"Total Months: {MonthCount}")
print(f"Total: ${NetProfit:,}")
print(f"Average Change: ${MeanMonthlyProfitChange:,.2f}")
print(f"Greatest Increase in Profits: {MaxGainMonth} (${MaxMonthlyGain:,})")
print(f"Greatest Decrease in Profits: {MaxLossMonth} (${MaxMonthlyLoss:,})")

# Open output file and write the results:
with open(OutputPath, "w", newline="") as WriteFile:
    print("Financial Analysis", file=WriteFile)
    print("------------------", file=WriteFile)
    print(f"Total Months: {MonthCount}", file=WriteFile)
    print(f"Total: ${NetProfit:,}",file=WriteFile)
    print(f"Average Change: ${MeanMonthlyProfitChange:,.2f}", file=WriteFile)
    print(f"Greatest Increase in Profits: {MaxGainMonth} (${MaxMonthlyGain:,})", file=WriteFile)
    print(f"Greatest Decrease in Profits: {MaxLossMonth} (${MaxMonthlyLoss:,})", file=WriteFile)

    