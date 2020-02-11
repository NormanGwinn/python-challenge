import csv
import sys

# A function to print election results
def PrintReport(fOut, dictCandidatesVotes, nVotes):
    fOut.write(f"Total Votes Cast:  {nVotes:,}\n\n")
    listCandidatesByVotesDescending = sorted(dictCandidatesVotes, key=dictCandidatesVotes.__getitem__, reverse=True)
    for candy in listCandidatesByVotesDescending:
        votes = dictCandidatesVotes[candy]
        fOut.write(f"{candy} received {int(votes):,} votes ({votes/(nVotes):2.2%})\n")  
    fOut.write(f"\nFirst Advancing Candidate:  {listCandidatesByVotesDescending[0]}\nSecond Advancing Candidate:  {listCandidatesByVotesDescending[1]}")

# Read the election results
sDataFile = r"C:\Users\norma\HDD_Documents\BootCamp\RU-HOU-DATA-PT-12-2019-U-C\Homework\03-Python-Challenge\Instructions\PyElections\Resources\houston_election_data.csv"
with open(sDataFile, newline='', encoding='utf-8') as csvDataFile:
    rdrDataFile = csv.reader(csvDataFile)
    iRow = 0
    # Use a dictionary to identify the unique candidates, and accumulate their votes
    dCandyweight = dict()
    for row in rdrDataFile:
        if iRow > 0:
            sCandyweight = row[0]
            if sCandyweight in dCandyweight:
                dCandyweight[sCandyweight] = dCandyweight[sCandyweight] + 1
            else:
                dCandyweight[sCandyweight] = 1
        iRow = iRow + 1

PrintReport(sys.stdout, dCandyweight, iRow - 1)
with open(r'\Users\norma\HDD_Documents\BootCamp\Assignments\03-Python-Challenge\python-challenge\PyElections\ElectionReport.txt', 'w') as fReport:
    PrintReport(fReport, dCandyweight, iRow - 1)

