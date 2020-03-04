#PyPoll Homework
import os
import csv

#lists storing data
candidate = []

# Directory
dir_path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join(dir_path, '..', '..', 'PyPoll_election_data.csv')
PyPoll_output_file = os.path.join(dir_path, 'PyPoll_outputfile.txt')

#Open CSV
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    candidate = [row[2] for row in csvreader]

#Create Empty Candidate Dictionary for Analysis
cand_dictionary = {}
unique_candidates = set(candidate)

#Number of Total Votes
total_votes = len(candidate)

#Dictionary created for - Vote Count and Percent Per Candidate
for name in unique_candidates:
    vote_count = candidate.count(name)
    percent_votes = round(((vote_count/total_votes)*100), 3)
    cand_dictionary[name] = [percent_votes, vote_count]

#Sort Dictionary by % Vote - Highest to Lowest
sorted_cand_dictionary = sorted(cand_dictionary.items(), key=lambda name: name[1], reverse=True)

#Election Result Analysis
print(
    f'Election Results'
    f'\n-------------------------'
    f'\nTotal Votes: {total_votes}'
    f'\n-------------------------'
)
for cand_stats in sorted_cand_dictionary:
    print(f'{cand_stats[0]}: {cand_stats[1][0]}% ({cand_stats[1][1]})')

print(
    f'-------------------------'
    f'\nWinner: {sorted_cand_dictionary[0][0]}'
    f'\n-------------------------'
)

#Write Answers to New Text File
with open(PyPoll_output_file, 'w') as outfile:
    outfile.write(
        f'Election Results'
        f'\n-------------------------'
        f'\nTotal Votes: {total_votes}'
        f'\n-------------------------'
    )
    for cand_stats in sorted_cand_dictionary:
        outfile.write(f'\n{cand_stats[0]}: {cand_stats[1][0]}% ({cand_stats[1][1]})')

    outfile.write(
        f'\n-------------------------'
        f'\nWinner: {sorted_cand_dictionary[0][0]}'
        f'\n-------------------------'
    )
    outfile.close()