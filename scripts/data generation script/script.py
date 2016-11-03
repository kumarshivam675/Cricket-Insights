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

id_num = 0

#resultFile = open("scorecard.csv", "w+")
cnt =0
for fnum in listdir("ipl"):
	name = "./ipl/" + str(fnum)
	print fnum
	f = open(name)
	match = yaml.safe_load(f)
	f.close()
	teams = match["info"]["teams"]
	t1 = teams[0]
	t2 = teams[1]
	print t1,t2
	innings = match["innings"]
	scorecard = {}
	for x in innings:
		for m in x:
			d = x[m]["deliveries"]
			t = x[m]["team"]
			if t == t1:
				o = t2
			else:
				o = t1
			for i in d:
				for j in i:
					batsman = i[j]["batsman"]
					bowler = i[j]["bowler"]
					runs = i[j]["runs"]["batsman"]
					total = i[j]["runs"]["total"]
	'''wr = csv.writer(resultFile,  quoting=csv.QUOTE_ALL)
	for x in scorecard:
		scorecard[x].insert(0,fnum[:-5])
		scorecard[x].insert(1,x)
		wr.writerow(scorecard[x])
	print cnt
	cnt+=1'''