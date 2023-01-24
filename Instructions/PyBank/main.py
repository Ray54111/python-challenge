import csv

csvpath = '/Users/rayzapien/Data/UCI-VIRT-DATA-PT-10-2022-U-LOLC/02-Homework/03-Python/Instructions/PyBank/budget_data.csv'

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile)
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    total_months=0
    max_profit=0
    min_profit=0
    total=0
    diff=0
    prev=0
    diff_sum=0
    for row in csvreader:
        change= int(row[1])
       
        total_months=total_months+1
        total= int(row[1])+total
        diff=int(row[1])-prev
        diff_sum=diff_sum - diff
        prev=int(row[1])
        if diff>max_profit:
            max_profit=diff
            max_date=row[0]
        elif diff<min_profit:
            min_profit=diff
            min_date=row[0]




    print("Finanacial Analysis")
    print("--------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total}")
    print(f"Average Change: $({diff_sum/total_months})")
    print(f"Greatest Increase in Profits: {max_date} (${max_profit})")
    print(f"Greatest Decrease in Profits: {min_date} (${min_profit})")