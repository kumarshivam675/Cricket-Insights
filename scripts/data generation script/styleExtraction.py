#Extracts batting and bowling style of players
#l = []
import csv
teamMap = {}

mapping = {'Right-arm medium' :('Right-arm','medium'), 'Right-arm offbreak':('Right-arm','offbreak'), 'Right-arm fast-medium':('Right-arm','fast-medium'), 'Legbreak googly':(None,'legbreak'), 'Right-arm medium-fast':('Right-arm','medium-fast'), 'Left-arm fast-medium':('Left-arm','fast-medium'), 'Slow left-arm orthodox':('Left-arm','slow'), 'Right-arm fast':('Right-arm','fast'), 'Slow left-arm chinaman':('Left-arm','slow'), 'Left-arm medium-fast':('Left-arm','medium-fast'), 'Legbreak':(None,'legbreak'), 'Right-arm medium, Right-arm offbreak':('Right-arm','medium;offbreak'), 'Right-arm bowler':('Right-arm', None), 'Left-arm medium':('Left-arm','medium'), 'Right-arm offbreak, Legbreak googly':('Right-arm','(offbreak;legbreak)'), 'Right-arm medium, Legbreak':('Right-arm','medium;legbreak'), 'Right-arm offbreak, Legbreak':('Right-arm','offbreak;legbreak'), 'Left-arm fast':('Left-arm','fast') , '' : (None , None)}

teamData = open('partnerships.csv' , 'r')
teamReader = csv.reader(teamData, delimiter=',')
for row in teamReader:
	if(row[0] not in teamMap):
		teamMap[row[0]] = row[2]

	if(row[1] not in teamMap):
		teamMap[row[1]] = row[2]

output = open('playersFinal.csv' , 'w')
with open('players.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	writer = csv.writer(output , delimiter = ',')
	count = 0
	#for row in reader:
	#	if(row[9] not in l):
	#		l.append(row[9])
	#print l
	
	for row in reader:
		bowl_attr = row.pop(9)
		if(count == 0):
			row.append('current_team')
			row.append('bowl_arm')
			row.append('bowl_style')
			count = count + 1
		else:
			if(row[5] in teamMap):
				row.append(teamMap[row[5]])
			else:
				row.append('NA')
			row.append(mapping[bowl_attr][0])
			row.append(mapping[bowl_attr][1])
		writer.writerow(row)



#print row[3]
#print row[9]
