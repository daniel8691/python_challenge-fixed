#modules
import os 
import csv


def daniel(daniels_file):
    # Read in CSV file
    dates = []
    Profit_Losses = []
    with open(daniels_file) as csvfile:
        csvReader = csv.reader(csvfile,delimiter=',')
        csvheader = next(csvReader)
        for row in csvReader:
            dates.append(row[0])
            Profit_Losses.append(int(row[1]))



    print("Financial Analysis")
    print("---------------------------------------")

    #The total number of months included in the dataset
    print("Total Months: " + str(len(dates)))
    #The net total amount of "Profit/Losses" over the entire period
    print("Total: " + str(sum(Profit_Losses)))
    #The average of the changes in "Profit/Losses" over the entire period
    sum_of_average_change = 0
    list_of_average_change = []
    for x in range(len(Profit_Losses)):
        if x == 0:
            continue
        average_change = ((Profit_Losses[x]) - Profit_Losses[x-1])
        list_of_average_change.append(average_change)
        sum_of_average_change = sum_of_average_change + average_change
                      

    print("Average Change: $" + str((sum_of_average_change) / (len(Profit_Losses)-1)))

    #The greatest increase in profits (date and amount) over the entire period
    max_value = max(list_of_average_change)
    index_max = list_of_average_change.index(max_value) 
    
    print("Greatest Increase in Profits: " + dates[index_max+1] + " ($"+ str(list_of_average_change[index_max]) + ")")

    #The greatest decrease in losses (date and amount) over the entire period
    min_value = min(list_of_average_change)
    index_min = list_of_average_change.index(min_value)
    print("Greatest Decrease in Profits: " + dates[index_min+1] + " ($" + str(list_of_average_change[index_min]) + ")")


daniel('budget_data.csv')