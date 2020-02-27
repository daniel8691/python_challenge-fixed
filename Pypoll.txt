#modules
import os
import csv 

#Read in CSV file
voter_id = []
county = []
candidate = []
with open('PyPoll.csv') as csvfile:
    csvReader = csv.reader(csvfile,delimiter = ',')
    csvheader = next(csvReader)
    for row in csvReader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

print("Election Results")
print("----------------------------")
# total number of voter cast
total_votes = len(voter_id)
print(total_votes)
print("----------------------------")
# list of candidates who received votes
unique_candidates = set(candidate)
print(list(unique_candidates))
print("----------------------------")
# percentage of votes for each candidate
candidate_khan = candidate.count("Khan")
percentage_khan = (candidate_khan / total_votes) * 100

candidate_correy = candidate.count("Correy")
percentage_correy = (candidate_correy / total_votes) * 100

candidate_li = candidate.count("Li")
percentage_li = (candidate_li / total_votes) * 100

candidate_tooley = candidate.count("O'Tooley")
percentage_tooley = (candidate_tooley / total_votes) * 100

print("Khan: " + str(round(percentage_khan,3)) + "% (" + str(candidate_khan) + ")")
print("Correy: " + str(round(percentage_correy,3)) + "% (" + str(candidate_correy) + ")")
print("Li: " + str(round(percentage_li,3)) + "% (" + str(candidate_li) + ")")
print("O'Tooley: " + str(round(percentage_tooley,3)) + "% (" + str(candidate_tooley) + ")")
print("----------------------------")
# total number of votes each candidates won

# winner of the election based on popular vote

all_candidates = []
all_candidates.append(candidate_khan)
all_candidates.append(candidate_correy)
all_candidates.append(candidate_li)
all_candidates.append(candidate_tooley)
if max(all_candidates) == candidate_khan:
    print("Winner: Khan")
elif max(all_candidates) == candidate_correy:
    print("Winner: Correy")
elif max(all_candidates) == candidate_li:
    print("Winner: Li")
else:
    print("Winner: O'Tooley")
print("----------------------------")