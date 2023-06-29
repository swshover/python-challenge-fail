# PyBank
import csv

# Open the file as read
with open('../Starter_Code/PyPoll/Resources/election_data.csv','r') as datafile:

    # Split the file out by commas
    data = csv.reader(datafile, delimiter=',')

    # Skip the header
    next(data)

    # Let's count the total votes first
    votes = 0

    # And a list of the people
    people = {}

    # Now we do the for loop
    for row in data:

        # Every row adds one to the votes
        votes += 1

        # This if statement will be to see if the name is in the people list
        if row[2] not in people:
            people[row[2]] = 0

        # Then we can use a for loop to count the votes per person in the dict
        people[row[2]] +=1
        # Now I have a dictionary with the total votes per person!

# Time to figure out the remaining stuff
# Let's make a percentages version for the people where I will store the votes
percentages={}

# We can use a for loop to add to this dictionary
for person in people:
    person_vote = people[person]
    percentage = round((person_vote/votes)*100,3)
    percentages[person] = percentage

# We can now find the winner through a few methods, let's do it with the votes dictionary
high_count = 0
high_person = None
for person in people:
    if people[person] > high_count:
        high_count = people[person]
        high_person = person

# Then we just print everything out now
print('Election Results')
print('-------------------------')
print(f'Total Votes: {votes}')
print('-------------------------')
for person in people:
    print(f'{person} : {percentages[person]}% ({people[person]})')
print('-------------------------')
print(f'Winner: {high_person}')
print('-------------------------')

# And write it to a text file per instructions
with open('Election_Results.txt','w') as text:
    text.write('Election Results\n')
    text.write('-------------------------\n')
    text.write(f'Total Votes: {votes}\n')
    text.write('-------------------------\n')
    for person in people:
        text.write(f'{person} : {percentages[person]}% ({people[person]})\n')
    text.write('-------------------------\n')
    text.write(f'Winner: {high_person}\n')
    text.write('-------------------------\n')
print('Done!')