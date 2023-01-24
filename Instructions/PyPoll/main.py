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
        if row[2] == "Diana DeGette":
            can_1 = str(row[2])
            can_1_votes += 1
        elif row[2] == "Charles Casper Stockham":
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

            
        



print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")
print(f"{can_1}: {can_1_votes}")
print(f"{can_2}: {can_2_votes} ")
print(f"{can_3}: {can_3_votes}")
print("-----------------------------")
print(f"Winner: {winner}")
print("-----------------------------")