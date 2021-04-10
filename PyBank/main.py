import os
import csv

#open and parse csv data
csv_path = os.path.join("Resources", "budget_data.csv")

with open(csv_path, 'r') as csv_file:
    bank_data = csv.reader(csv_file, delimiter = ',')
    header_row = next(bank_data)

    dates = []
    profits = []
    p_deltas = [] #monthly changes in profits
    
    num = None #starter for calculating monthly deltas

    for row in bank_data:
        date = row[0]
        profit = float(row[1])
        
        dates.append(date)
        profits.append(profit)
        
        #calculate monthly change in profits
        if num != None:
            num1 = float(row[1])
            delta = num1 - num
            p_deltas.append(delta)
            num = num1
        else:
            num = float(row[1])

    #the cvs file contains monthly data, the # of months is equal to the number of rows - 1,
    #In case there might be a duplicate in there, I set them to get the unique values
    date_set = set(dates)
    count_unique_dates = len(date_set)
    
    #calculate net profit
    net_profit = sum(profits)

    #calculate average change in monthly profits
    avg_p_delta = sum(p_deltas)/len(p_deltas)

    #calculate max and min profits
    mx = max(p_deltas)
    mx_index = p_deltas.index(mx)
    mx_date = dates[mx_index + 1]

    mn = min(p_deltas)
    mn_index = p_deltas.index(mn)
    mn_date = dates[mn_index + 1]
    
    #format results
    analysis = (f"""
    Financial Analysis
    -------------------------------
    Total Months:  {count_unique_dates}
    Total:  {"${:,.2f}".format(net_profit)}
    Average Change:  {"${:,.2f}".format(avg_p_delta)}
    Greatest Increase in Profits:  {mx_date}  ({"${:,.2f}".format(mx)})
    Greatest Decrease in Profits: {mn_date}({"${:,.2f}".format(mn)}) """)
    
    #create a txt file / write results / close file
    txt_path = os.path.join("analysis", "results.txt")
    txt_file = open(txt_path, 'w')
    txt_file.write("String Variable: {}".format(analysis))
    txt_file.close()
    
    #print results to terminal
    print(analysis)