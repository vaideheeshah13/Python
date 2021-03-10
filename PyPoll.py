#import data
import os
import csv

PyPollcsv = os.path.join("/Users/Vaidehee/nu-chi-data-pt-02-2021-u-c-master/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")

#defining variables and list

count = 0
total_candidates = []
candidate_name = []
voter_count = []
voter_percent = []
total_votes = 0

#open csv file

with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
#loop through csv file to count # votes

    for row in csvreader:
        count = count + 1
        total_candidates.append(row[2])

    for i in set(total_candidates):
        candidate_name.append(i)
        votes_candidate = total_candidates.count(i)
        voter_count.append(votes_candidate)
#percent
        percent = (votes_candidate/count)*100

        voter_percent.append(percent)

#find the winner
winning_vote = max(voter_count)
winner = candidate_name[voter_count.index(winning_vote)]

#print values
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(candidate_name)):
             print(f"{candidate_name[i]}: {round(voter_percent[i],2)}00% ({str(voter_count[i])})")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")
#print to .txt file
with open('results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(candidate_name)):
             text.write(f"{candidate_name[i]}: {round(voter_percent[i],2)}00% ({str(voter_count[i])})")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")
