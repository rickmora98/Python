<h1> PyBank and PyPoll <br> (Two examples of Python coding) </h1>

In PyBank, the progam (main.py) reads data from CSV file "budget_data.csv" and calculates
the total number of months of financial data, the overall net profit
or loss, the month with the largest increase in profit from it's
previous month, the month with the largest decrease in profit from it's
previous month, and the average of the monthly changes in profit.
The results are placed into file "budget_summary.txt" and are also
displayed to the console.

In PyPoll, the program (main.py) reads data from CSV file "election_data.csv" and counts
how many total votes were cast, who the candidates were, and how
many votes each received as well as their percent of total votes,
and also who the overall winner was.  The results are placed into
file "election_summary.txt" and are also displayed to the console.


Main Folders:

"PyBank" contents:
	"main.py": python script for the profit analysis part of the assignment
	"Resources": folder containing file "budget_data.csv" (input file)
	"Analysis": folder containing file "budget_summary.txt" (output file)


"PyPoll" contents:
	"main.py" python script for the election analysis part of the assignment.
  	"Resources": folder containing file"election_data.csv" (input file)
	"Analysis": folder containing file "election_summary.txt" (output file)

Notes:

The python scripts rely on relative path referencing, therefore the folders "Resources" 
and "Analysis" should not be deleted, moved, or renamed.  Also, the input files must be
present in the "Resources" folders and not be renamed.
If the output files already exist in the "Analysis" folders prior to executing the code,
they will be replaced by the new output files.

	
 
