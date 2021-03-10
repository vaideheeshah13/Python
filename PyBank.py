#import 
import os
import csv

PyBankcsv = os.path.join("/Users/Vaidehee/nu-chi-data-pt-02-2021-u-c-master/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")
#create variables and lists

date =[]
profit = []
monthly_changes = []


month = 0
total_profit_change = 0
initial_profit = 0
final_profit = 0
monthly_change_profits = 0
average_change = 0
greatest_increase_date = 0
greatest_decrease_date = 0
greatest_increase_profits = 0
greatest_decrease_profits = 0

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
#count number of months - loop through
    for row in csvreader:
        month = month + 1
#TOTAL PROFIT
        profit.append(row[1])
        total_profit_change = total_profit_change + int(row[1])
#Final profit

        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit
        
        monthly_changes.append(monthly_change_profits)

        total_profit_change = total_profit_change + monthly_change_profits
        initial_profit = final_profit
#average change

        average_change = (total_profit_change/monthly_change_profits)
       
        date.append(row[0])
#greatest increase/decrease in profits 

        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

        greatest_increase_date = date[monthly_changes.index(greatest_increase_profits)]
        greatest_decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

# print

    print("Financial Analysis")
    print("============================================")
    print("Total Months: " + str(month))
    print("Total Revenue: " + "$" +str(total_profit_change))
    print("Average Change: " + "$" + str(int(average_change)))
    print("Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " +str(greatest_decrease_date)+ " ($" + str(greatest_decrease_profits)+ ")")

# print to text
with open('analysis.txt', 'w') as text:
    text.write("-------------------------------------------------\n")
    text.write(" Financial Analysis" + "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(month) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit_change) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")
