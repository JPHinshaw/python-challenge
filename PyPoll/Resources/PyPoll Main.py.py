import os
import csv

inputFile = os.path.join("election_data.csv")
outputFile = os.path.join("ElectionDataAnalysis.txt")

#variables
totalVotes = 0
candidates = []
candidateVotes = {}
winningCount = 0
winningCandidate = ""




with open(inputFile) as electionData:
    csvreader = csv.reader(electionData)

    header = next(csvreader)

    for row in csvreader:
        totalVotes += 1

        if row[2] not in candidates:
            candidates.append(row[2])

            candidateVotes[row[2]] = 1
        else:
            candidateVotes[row[2]] += 1

voteCount = ""
voteOutput = ""
for candidates in candidateVotes:
    votes = candidateVotes.get(candidates)
    votePct = (float(votes) / float(totalVotes)) * 100.000

    voteOutput += f"\t{candidates}: {votePct:.2f}%: {(votes)} \n"
    voteCount += f"\t{candidates}: {votes}"
#print(voteCount)
if votes > winningCount:
    winningCount = votes
    winningCandidate = candidates
    #print(votes)
winningCandidateOutput = f"Winner: {winningCandidate}\n-----------------------------"

#create an output variable to hold the output
output = (
    f"\n\nSurvey Results\n"
    f"---------------------------\n"
    f"\tTotal Votes: {totalVotes:,}\n"
    f"----------------------------- \n"
    f"{voteOutput} \n"
    f"-------------------------------\n"
    f"{winningCandidateOutput}"
    
)
print(output)
with open(outputFile, "w") as textFile:
    textFile.write(output)