# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

diff = []

fhand=open('football.csv')

for line in fhand:
    line=line.rstrip().split(',')
    #Find the score difference for each individual team
    if line[5]=='Goals':
        continue
    delta=int(line[5])-int(line[6])
    diff.append((delta,line[0]))
#sort list from largest goal difference
diff.sort(reverse=True)
[print (i[1], i[0]) for i in diff]

print ('The largest goal difference this season was %s with a goal difference of %d!' % (diff[0][1], diff[0][0]))
