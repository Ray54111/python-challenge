import csv
import os

#this os path didn't work I did relative path 
#csvpath = os.path.join("..","PyBank","Resources","budget_data.csv")
csvpath = "02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"
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
    month_avg=0
    diff_list=[]

    #establish first row to not interfere with the average change
    first_row=next(csvreader)
    total=int(first_row[1])
    prev=int(first_row[1])
    total_months= total_months+1

 

    for row in csvreader:
        current=int(row[1])
        #track the total months
        total_months=total_months+1
        #count the total 
        total= current+total
        #adding the difference between months 
        diff=current-prev
        prev=current
        diff_list+=[diff]
       
        
        #count the max monthly profit
        if diff>max_profit:
            max_profit=diff
            max_date=row[0]
        #count the profit loss
        elif diff<min_profit:
            min_profit=diff
            min_date=row[0]

#m counts the total months between the 
m=total_months-1
diff_sum=sum(diff_list)
month_avg=sum(diff_list)/(m)
#used to check
print(f"{m}")
print(f"{diff_sum}")
print(f"{month_avg}")


print("Finanacial Analysis")
print("--------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: $({month_avg:.2f})")
print(f"Greatest Increase in Profits: {max_date} (${max_profit})")
print(f"Greatest Decrease in Profits: {min_date} (${min_profit})")

financial_analysis=(
    f"Finanacial Analysis\n"
    f"--------------------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total}\n"
    f"Average Change: $({month_avg:.2f})\n"
    f"Greatest Increase in Profits: {max_date} (${max_profit}\n"
    f"Greatest Decrease in Profits: {min_date}(${min_profit}\n"

)

with open('02-Homework/03-Python/Instructions/PyBank/financial_analysis.txt','w') as txt_file:
    txt_file.write(financial_analysis)