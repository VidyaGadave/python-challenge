# Import the os module and CSV module
import os
import csv

#Declaring variables
months_list = []
pnl_list =[]
difference_list = []

# Module for reading CSV files
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvhandler:
    csvreader = csv.reader(csvhandler,delimiter=",")

    csv_header = next(csvreader)    #Getting headers

    for row in csvreader:
        months_list.append(row[0])
        pnl_list.append(int(row[1]))

#Calculcate total number of months
total_mon =len(months_list)

#Calculcate total sum of Profit and Loss
total_sum = sum(pnl_list)

#Calculcate max increase and max decrease in profit
max_inc_profit = 0
max_dec_profit = 0

for i in range(1,len(pnl_list)):
    difference_list.append(pnl_list[i]-pnl_list[i-1])

max_inc_profit=max(difference_list)
max_dec_profit=min(difference_list)

# Get matching month for change from months list
max_inc_profit_mon=(months_list[difference_list.index(max_inc_profit)+1])
max_dec_profit_mon=(months_list[difference_list.index(max_dec_profit)+1])

# Calculate Avergae change
avg_change = round(sum(difference_list)/len(difference_list),2)


#Printing all the results
print("Financial Analysis")
print("------------------------------------------")
print(f"Total Months : {total_mon}")
print(f"Total : ${total_sum}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {max_inc_profit_mon}  (${max_inc_profit})")
print(f"Greatest Decrease in Profits: {max_dec_profit_mon}  (${max_dec_profit})")


#Writing all data to text file
output_file = os.path.join('Analysis', 'PyBank_Output.txt')

with open(output_file, 'w') as writer_handle:
    print("Financial Analysis",file=writer_handle)
    print("------------------------------------------", file=writer_handle)
    print(f"Total Months : {total_mon}", file=writer_handle)
    print(f"Total : ${total_sum}", file=writer_handle)
    print(f"Average Change: ${avg_change}", file=writer_handle)
    print(f"Greatest Increase in Profits: {max_inc_profit_mon}  (${max_inc_profit})", file=writer_handle)
    print(f"Greatest Decrease in Profits: {max_dec_profit_mon}  (${max_dec_profit})", file=writer_handle)
