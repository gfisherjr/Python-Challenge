# PyBank Homework
import os
import csv
import statistics

#lists storing data
dates = []
profit_loss = []
monthly_change = []

new_pybank_list = zip(dates, profit_loss, monthly_change)
new_pybank_list2 = zip(dates, profit_loss, monthly_change)

# Directory
dir_path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join(dir_path, '..', '..', 'PyBank_budget_data.csv')
output_file = os.path.join(dir_path, 'outputfile.txt')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) 
  
    for row in csvreader:    
        dates.append(row[0])
        profit_loss.append(int(row[1]))

#Calculate Monthly Change
for i in range(len(profit_loss) - 1):
    change = (profit_loss[i + 1] - profit_loss[i])
    monthly_change.append(change)

#insert value of zero in first element of monthly_change list
monthly_change.insert(0, 0) 

#Calculate Average Monthly Change
average_monthly_change = round(statistics.mean(monthly_change[1:]), 2)

#Greatest Increase and Decrease in Profits:
max_tuple = max((new_pybank_list), key=lambda x: x[2])
min_tuple = min((new_pybank_list2), key=lambda y: y[2])

print('\nFinancial Analysis'
    f'\n--------------------------'
    f'\nTotal Months: {len(dates)}'
    f'\nTotal: ${sum(profit_loss)}'
    f'\nAverage Change: ${average_monthly_change}'
    f'\nGreatest Increase in Profits: {max_tuple[0]} (${max_tuple[2]})'
    f'\nGreatest Decrease in Profits: {min_tuple[0]} (${min_tuple[2]})'
)

with open(output_file, 'w') as outfile:
    outfile.write('Financial Analysis'
                f'\n--------------------------'
                f'\nTotal Months: {len(dates)}'
                f'\nTotal: ${sum(profit_loss)}'
                f'\nAverage Change: ${average_monthly_change}'
                f'\nGreatest Increase in Profits: {max_tuple[0]} (${max_tuple[2]})'
                f'\nGreatest Decrease in Profits: {min_tuple[0]} (${min_tuple[2]})'
    )
    outfile.close()