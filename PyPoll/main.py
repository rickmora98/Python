'''
Program: 
   main.py

Written by: 
   Ricardo G. Mora, Jr  09/28/2021

Description:
   This progam reads data from CSV file "election_data.csv" and counts
   how many total votes were cast, who the candidates were, and how
   many votes each received as well as their percent of total votes,
   and also who the overall winner was.  The results are placed into
   file "election_summary.txt" and are also displayed to the console.
'''

# Import modules:
import os
import csv

# Set relative paths to input and output files:
InputPath = os.path.join("Resources", "election_data.csv")
OutputPath = os.path.join("Analysis", "election_summary.txt")

# Initialize variables:
TotalVotes = 0
MostVotesReceived = 0
Winner = ""
ElectionResults = {}  # Dictionary to hold candidate names and their respective vote counts

# Open input file and read into csv reader:
with open(InputPath, "r", newline="") as ReadFile:
    DataReader = csv.reader(ReadFile, delimiter=",")

    # Skip header row:
    HeaderRow = next(DataReader)

    # Loop through remaining rows, increment VoteCount, and extract candidate data:
    for Row in DataReader:
        TotalVotes = TotalVotes + 1
        Candidate = Row[2]

        # If the candidate is already in ElectionResults, increment his/her vote count
        # Otherwise, add them to ElectionResults with an initial vote count of 1:
        if Candidate in ElectionResults.keys():
            ElectionResults[Candidate] = ElectionResults[Candidate] + 1
        else:
            ElectionResults[Candidate] = 1

# Output the results to the terminal:
print("Election Results")
print("--------------------------")
print(f"Total Votes: {TotalVotes:,}")
print("--------------------------")

# Loop through all the candidates:
for ThisCandidate, VotesReceived in ElectionResults.items():
    print(f"{ThisCandidate}: {100 * VotesReceived / TotalVotes :.3f}% ({VotesReceived:,})")
        
    # Determine who received the most votes:
    if VotesReceived > MostVotesReceived:
        MostVotesReceived = VotesReceived
        Winner = ThisCandidate

print("--------------------------")
print(f"Winner: {Winner}")
print("--------------------------")

# Output the same results to the output file:
with open(OutputPath, "w", newline="") as WriteFile:
    print("Election Results", file=WriteFile)
    print("--------------------------", file=WriteFile)
    print(f"Total Votes: {TotalVotes:,}", file=WriteFile)
    print("--------------------------", file=WriteFile)

    # Loop through all the candidates:
    for ThisCandidate, VotesReceived in ElectionResults.items():
        print(f"{ThisCandidate}: {100 * VotesReceived / TotalVotes :.3f}% ({VotesReceived:,})", file=WriteFile)
        
    print("--------------------------", file=WriteFile)
    print(f"Winner: {Winner}", file=WriteFile)
    print("--------------------------", file=WriteFile)
  