import csv

csvpath = '/Users/rayzapien/Data/UCI-VIRT-DATA-PT-10-2022-U-LOLC/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv'

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    total_votes=0
    
    can_1_votes=0
    can_2_votes=0
    can_3_votes=0


    for row in csvreader:
        total_votes += 1
        if row[2] == "Charles Casper Stockham":
            can_1 = str(row[2])
            can_1_votes += 1
        elif row[2] == "Diana DeGette":
            can_2 =str(row[2])
            can_2_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            can_3 = str(row[2])
            can_3_votes += 1
    if can_1_votes>can_2_votes and can_1_votes>can_3_votes:
         winner=can_1
    elif can_2_votes>can_1_votes and can_2_votes>can_3_votes:
        winner=can_2
    elif can_3_votes>can_1_votes and can_3_votes>can_2_votes:
        winner=can_3

can_1_percent=can_1_votes/total_votes*100
can_2_percent=can_2_votes/total_votes*100       
can_3_percent=can_3_votes/total_votes*100


print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")
print(f"{can_1}: {can_1_percent:.2f}% {can_1_votes} votes")
print(f"{can_2}: {can_2_percent:.2f}% {can_2_votes} votes")
print(f"{can_3}: {can_3_percent:.2f}% {can_3_votes} votes")
print("-----------------------------")
print(f"Winner: {winner}")
print("-----------------------------")

election_results=(
    f"Election Results\n"
    "-----------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-----------------------------\n"
    f"{can_1}: {can_1_percent:.2f}% {can_1_votes} votes\n"
    f"{can_2}: {can_2_percent:.2f}% {can_2_votes} votes\n"
    f"{can_3}: {can_3_percent:.2f}% {can_3_votes} votes\n"
    "-----------------------------\n"
    f"Winner: {winner}\n"
    "-----------------------------\n"
)

with open('02-Homework/03-Python/Instructions/PyPoll/election_results.txt','w') as txt_file:
    txt_file.write(election_results)