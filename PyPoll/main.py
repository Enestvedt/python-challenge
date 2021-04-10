import os
import csv

#import csv file and parse data
csv_path = os.path.join("Resources", "election_data.csv")

with open(csv_path) as csv_file:
    election_data = csv.reader(csv_file, delimiter=',')
    print(election_data)

    header = next(election_data)

    candidates = []

    for row in election_data:
        candidate = row[2]
        candidates.append(candidate)

    #calculations
    total_votes = len(candidates)

    candidate_list = list(set(candidates))

    #use comprehension to tally the count of each candidate name an calculate percent 
    vtally = [[x, "{:.0%}".format(candidates.count(x)/total_votes), candidates.count(x)] for x in candidate_list]

    #set a dynamic variable for each canbdidate to help with printing/exporting
    for i in range(0, len(vtally)):
        globals()[f"candidate{i}"] = f"{vtally[i][0]}:  {vtally[i][1]}    ({vtally[i][2]})"

    #searches for max value in nested list returns as a list
    w1 = max(vtally, key=lambda x: x[1])
    winner = w1[0]
    
#format results text 
prt_rslt = (f"""
Election Results
---------------------------------
Total Votes:  {total_votes}
---------------------------------
{candidate0}
{candidate1}
{candidate2}
{candidate3}
---------------------------------
Winner:  {winner}
----------------------------------""")

#create a txt file / write results / close file
txt_path = os.path.join("analysis", "results.txt")
txt_file = open(txt_path, 'w')
txt_file.write("String Variable: {}".format(prt_rslt))
txt_file.close()

#print results to terminal
print(prt_rslt)
