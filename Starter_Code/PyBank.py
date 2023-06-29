# PyBank
import csv

# Open the file as read
with open('../Starter_Code/PyBank/Resources/budget_data.csv','r') as datafile:

    # Split the file out by commas
    data = csv.reader(datafile, delimiter=',')

    # Skip the header
    next(data)

    # We need to set up some initial variables now
    total = 0
    months = 0

    # We will use this list to find the average change price later on.
    changes = []
    # We will also need an initial value of None to work with set to no value so
    # that we can have it built into an if statement later
    prev_month = None

    # For greatest and least, we can make some quick 0 values to use as a start
    greatest = 0
    least = 0

    # And we need the corresponding months as None
    high_month = None
    low_month = None


    # Calculate the total by using a for loop through the rows
    for row in data:

        #This takes care of the total and months
        total += int(row[1])
        months += 1

        # Now we have to add to changes list so we can find the average
        # Need to remember the first line has no change (it's empty)
        if prev_month != None:

            # Now we can call change equal to the change between the months
            change = int(row[1]) - prev_month

            # And add it to our existing list
            changes.append(change)

            if change > greatest:
                greatest = change
                high_month = str(row[0])
            if change < least:
                least = change
                low_month = str(row[0])

        # The previous month needs to change as we loop through the rows
        # That means it needs to go outside the if statement
        prev_month = int(row[1])

average = sum(changes)/len(changes)

# Print to text file
with open('Financial_Analysis.txt','w') as text:
    text.write('Financial Analysis\n')
    text.write('----------------------------\n')
    text.write(f'Total Months: {months}\n')
    text.write(f'Total: ${total}\n')
    text.write(f'Average Change: ${average}\n')
    text.write(f'Greatest Increase in Profits: {high_month} (${greatest})\n')
    text.write(f'Greatest Decrease in Profits: {low_month} (${least})\n')

# Print to terminal
print('Financial Analysis\n')
print('----------------------------\n')
print(f'Total Months: {months}\n')
print(f'Total: ${total}\n')
print(f'Average Change: ${average}\n')
print(f'Greatest Increase in Profits: {high_month} (${greatest})\n')
print(f'Greatest Decrease in Profits: {low_month} (${least})\n')
print('Done!')
