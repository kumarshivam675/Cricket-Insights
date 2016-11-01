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

resultFile = open("scorecard.csv", "w+")
cnt = 0
for fnum in listdir("ipl"):
    name = "./ipl/" + str(fnum)
    print fnum
    f = open(name)
    match = yaml.safe_load(f)
    f.close()
    teams = match["info"]["teams"]
    t1 = teams[0]
    t2 = teams[1]
    print t1, t2
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
                    if batsman in scorecard:
                        scorecard[batsman][0] += runs
                    else:
                        scorecard[batsman] = [runs, 0, 0, 0, "", "", 0, 0, 0, t]
                    if bowler in scorecard:
                        scorecard[bowler][6] += total
                    else:
                        scorecard[bowler] = [0, 0, 0, 0, "", "", total, 0, 0, o]
                    scorecard[batsman][1] += 1
                    scorecard[bowler][7] += 1
                    if runs == 4:
                        scorecard[batsman][2] += 1
                    elif runs == 6:
                        scorecard[batsman][3] += 1
                    if "wicket" in i[j]:
                        kind = i[j]["wicket"]["kind"]
                        player_out = i[j]["wicket"]["player_out"]
                        if player_out not in scorecard:
                            scorecard[player_out] = [0, 0, 0, 0, "", "", 0, 0, 0, t]
                        scorecard[player_out][4] = bowler
                        scorecard[player_out][5] = kind
                        if kind != "run out":
                            scorecard[bowler][8] += 1
    wr = csv.writer(resultFile, quoting=csv.QUOTE_ALL)
    for x in scorecard:
        scorecard[x].insert(0, fnum[:-5])
        scorecard[x].insert(1, x)
        wr.writerow(scorecard[x])
    print cnt
    cnt += 1
