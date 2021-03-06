## The main Program
## Get summary of matches from the dataset

## Match_id, Team1_id, Team2_id, Venue, Toss, Elected_to, Win_team, loser, Date, Win_by_runs, Win_by_wickets
## Match_id = file_name
## Team1 -> Home Team
## Venue -> city
## Toss -> winner Team name
## Elected_to ->


import yaml
from os import listdir
import csv
from math import floor
id_num = 0

resultFile = open("runs_per_over.csv", "w+")
cnt =0
overs = [0]*20
bowls = [0]*20
data = {}
for fnum in listdir("../../data"):
	name = "../../data/" + str(fnum)
	print fnum
	f = open(name)
	match = yaml.safe_load(f)
	f.close()
	year = match["info"]["dates"][0].year
	innings = match["innings"]
	scorecard = {}
	for x in innings:
		for m in x:
			d = x[m]["deliveries"]
			t = x[m]["team"]
			for i in d:
				for j in i:
					batsman = i[j]["batsman"]
					bowler = i[j]["bowler"]
					runs = i[j]["runs"]["batsman"]		
					total = i[j]["runs"]["total"]
					overs[int(j)]+=total
					bowls[int(j)]+=1
					if(t,year,int(j)) in data:
						data[(t,year,int(j))][0] +=total 
						data[(t,year,int(j))][1] +=1
					else:
						data[(t,year,int(j))] = [0,0,0]
						data[(t,year,int(j))][0] = total 
						data[(t,year,int(j))][1] = 1
						data[(t,year,int(j))][2] = 0
					if "wicket" in i[j]:
						data[(t,year,int(j))][2] += 1

	'''
	wr = csv.writer(resultFile, quoting=csv.QUOTE_ALL)
	for x in scorecard:
		scorecard[x].insert(0,fnum[:-5])
		scorecard[x].insert(1,x)
		wr.writerow(scorecard[x])'''
	print cnt
	cnt+=1
	#print data
#runrate = [b*6.0 / (m) for b,m in zip(overs, bowls)]
wr = csv.writer(resultFile, quoting=csv.QUOTE_ALL)
for x in data:
	print x[0],x[1],x[2]+1,data[x][0],data[x][2], data[x][1]
	wr.writerow([x[0],x[1],x[2]+1,data[x][0],data[x][2], data[x][1], (data[x][0]*6.0)/data[x][1], (data[x][2]*6.0)/data[x][1]])