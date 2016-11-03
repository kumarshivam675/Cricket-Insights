import csv
#openFile = open("team_summary.csv", "w+")

with open('team_summary.csv', 'rb') as csvfile:
	rdr = csv.reader(csvfile)
	excel ={}
	for row in rdr:
		if (row[4],row[1][1::]) in excel:
			excel[(row[4],row[1][1::])][0]+=1
		else:
			excel[(row[4],row[1][1::])]= [1,0]

		if (row[4],row[2]) in excel:
			excel[(row[4],row[2])][0]+=1
		else:
			excel[(row[4],row[2])]= [1,0]

		excel[(row[4],row[7])][1] += 1

with open('location_team_wins.csv','w+') as csvfile:
	wr = csv.writer(csvfile)
	for i in excel:
		wr.writerow([i[0],i[1],excel[i][0],excel[i][1]])
