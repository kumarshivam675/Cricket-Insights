import csv
#openFile = open("team_summary.csv", "w+")

with open('batsman_vs_bowler_total.csv', 'rb') as csvfile:
	rdr = csv.reader(csvfile)
	excel ={}
	cnt = 0
	for row in rdr:
		if cnt == 0:
			cnt=1
			continue
		if row[0] == '':
			break
		if row[0] in excel:
			excel[row[0]][0]+=int(row[10])
			excel[row[0]][1]+=int(row[9])
			excel[row[0]][2]+=int(row[14])			
		else:
			excel[row[0]]= [int(row[10]),int(row[9]),int(row[14]) , row[11]]

with open('average.csv','w+') as csvfile:
	wr = csv.writer(csvfile)
	for i in excel:
		if excel[i][1] == 0:
			avg = excel[i][0]*1.0
		else:
#			print excel
			avg = excel[i][0]*1.0/excel[i][1]

		wr.writerow([i,excel[i][0],excel[i][1],excel[i][2],(excel[i][0]*100.0)/excel[i][2],avg,excel[i][3]])
