# ## PyPoll
# 
# * In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, 
# but unfortunately, his concentration isn't what it used to be.)
# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
#   * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.
# * As an example, your analysis should look similar to the one below:
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   ------------------------
# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import csv
# track of candidates and their votes in two separate lists 
Candidates = []
CandidateVotes = []
VoteCount = 0
WinnerVotes = 0
with open("../Resources/election_data.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip first row headers
    next(csvreader, None)
    for row in csvreader:
        #Increment the vote counter
        VoteCount += 1
        #If the candidate does not appear in the list of candidates, add them (append) to the list and add (apend) them to the votes list 
        if Candidates.count(row[2]) == 0:
            Candidates.append(row[2])
            CandidateVotes.append(1)
        else:
            #If the candidate already appears, increment their vote count
            CandidateVotes[Candidates.index(row[2])] += 1

#Print results to the screen
print("Election Results\n")
print("-------------------------")
print(f"Total Votes: {VoteCount}\n")
print("-------------------------")
#Run through the candidate list
for n in range(len(Candidates)):
    #candidate name printed, perc of votes they received , number of votes they received
    print(f"{Candidates[n]}: {(CandidateVotes[n]/VoteCount):.2f} ({CandidateVotes[n]})")
    
#was the current candidate the highest vote getter, then save their name , vote count as the new winner
if CandidateVotes[n] > WinnerVotes:
        WinnerName = Candidates[n]
        WinnerVotes = CandidateVotes[n]
print("-------------------------")
#Print winner name
print(f"Winner: {WinnerName}")
print("-------------------------")

#output to text file
with open("Election_Results.txt","w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {VoteCount}\n")
    txtfile.write("-------------------------\n")
    for n in range(len(Candidates)):
        txtfile.write(f"{Candidates[n]}: {(CandidateVotes[n]/VoteCount):.2f} ({CandidateVotes[n]})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {WinnerName}\n")
    txtfile.write("-------------------------\n")