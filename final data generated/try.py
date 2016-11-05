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
		if row[1] == '':
			break
		if row[1] in excel:
			excel[row[1]][0]+=int(row[10])
			excel[row[1]][1]+=int(row[9])
			excel[row[1]][2]+=int(row[14])

			excel[row[1]][3]+=int(row[2])
			excel[row[1]][4]+=int(row[3])
			excel[row[1]][5]+=int(row[4])
			excel[row[1]][6]+=int(row[5])
			excel[row[1]][7]+=int(row[6])
			excel[row[1]][8]+=int(row[8])	
		else:
			excel[row[1]]= [int(row[10]),int(row[9]),int(row[14]) , int(row[2]) , int(row[3]) , int(row[4]) , int(row[5]) , int(row[6]) , int(row[8]) ,row[11]]

with open('bowlers_average.csv','w+') as csvfile:
	wr = csv.writer(csvfile)
	#wr.writerow('Name','Runs','Wickets','Balls','Strike_rate','Avg','')
	for i in excel:
		if excel[i][1] == 0:
			avg = excel[i][0]*1.0
		else:
#			print excel
			avg = excel[i][0]*1.0/excel[i][1]

		wr.writerow([i,excel[i][0],excel[i][1],excel[i][2],(excel[i][0]*6.0)/excel[i][2],avg,excel[i][3],excel[i][4],excel[i][5],excel[i][6],excel[i][7],
		excel[i][8]])
