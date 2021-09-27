
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
    
    HeaderRow = next(DataReader) # Skip header row
    FirstRow = next(DataReader) # Look at first row of data

    # Initialize variables:
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

# Calculate the average of all changes in monthly profits:
#         = ((R2-R1) + (R3-R2) + (R4-R3) + ... + (R85 - R84) + (R86 - R85) ) / (n-1)
#         = (R2 - R1 + R3 - R2 + R4 - R3 + ... + R85 - R84 + R86 - R85) / (n-1)
#         = (R86 - R1) / (n-1)
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

    