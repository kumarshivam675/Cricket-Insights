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
final = [0]*11
balls = [0]*11
outs = [0]*11
for fnum in listdir("ipl"):
	name = "./ipl/" + str(fnum)
	print fnum
	f = open(name)
	match = yaml.safe_load(f)
	f.close()
	teams = match["info"]["teams"]
	t1 = teams[0]
	t2 = teams[1]
	innings = match["innings"]
	for x in innings:
		for m in x:
			order = {}
			next =0
			d = x[m]["deliveries"]
			t = x[m]["team"]
			for i in d:
				for j in i:
					batsman = i[j]["batsman"]
					non_striker = i[j]["non_striker"]
					runs = i[j]["runs"]["batsman"]		
					total = i[j]["runs"]["total"]
					if batsman not in order:
						next+=1
						order[batsman] = next
					if non_striker not in order:
						next+=1
						order[non_striker] = next
					if "wicket" in i[j]:
						outs[order[i[j]["wicket"]["player_out"]]-1]+=1
					#print order
					final[order[batsman]-1] += runs
					balls[order[batsman]-1] += 1
					if "extras" in i[j]:
						if "wides" in i[j]["extras"] or "noballs" in i[j]["extras"]:
							balls[order[batsman]-1] -=1


	'''
	wr = csv.writer(resultFile,  quoting=csv.QUOTE_ALL)
	for x in scorecard:
		scorecard[x].insert(0,fnum[:-5])
		scorecard[x].insert(1,x)
		wr.writerow(scorecard[x])'''
	print cnt
	cnt+=1
print final
print balls
print outs
strikerate = [(b*100.0) / m for b,m in zip(final, balls)]
average = [(b*1.0) / m for b,m in zip(final, outs)]
print strikerate
print average

wr = csv.writer(resultFile,  quoting=csv.QUOTE_ALL)
for a,b,c,d,e in zip(final,balls,outs,strikerate,average):
	wr.writerow([a,b,c,d,e])
