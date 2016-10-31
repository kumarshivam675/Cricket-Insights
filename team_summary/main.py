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
import sys

id_num = 0

csv = open("team_summary.csv", "w+")
head =     "Match_id, Team1_id, Team2_id, Venue, City, Toss, Elected_to, Win_team, loser, Date, Win_by_runs, Win_by_wickets\n"
csv.write(head)

errors = []


for i in listdir("dataset"):
    print(i)
    name = "./dataset/" + str(i)
    f = open(name)
    match = yaml.safe_load(f)
    f.close()

    #print (match)
    try:
        info = match["info"]
        match_id = i.split(".")[0]
    #    print(info)

        """
        {'city': 'Chandigarh', 'dates': [datetime.date(2010, 3, 13)],
        'match_type': 'T20', 'gender': 'male', 'venue': 'Punjab Cricket Association Stadium, Mohali',
        'competition': 'IPL', 'teams': ['Kings XI Punjab', 'Delhi Daredevils'],
        'umpires': ['BR Doctrove', 'S Ravi'],
        'toss': {'decision': 'field', 'winner': 'Delhi Daredevils'},
        'player_of_match': ['G Gambhir'],
        'outcome': {'winner': 'Delhi Daredevils', 'by': {'wickets': 5}},
        'overs': 20}
        """

        team1 = info["teams"][0]
        team2 = info["teams"][1]
        venue = info["venue"].replace(",", " ")
        city = info["city"]
        toss = info["toss"]["winner"]
        elected_to = info["toss"]["decision"]
        win_team = info["outcome"]["winner"]
        if(win_team == team1):
            loser_team = team2
        else:
            loser_team = team1
        date = info["dates"][0]
        if("runs" in info["outcome"]["by"]):
            win_rums = info["outcome"]["by"]["runs"]
        else:
            win_rums = 0
        if("wickets" in info["outcome"]["by"]):
            win_wickets = info["outcome"]["by"]["wickets"]
        else:
            win_wickets = 0


    ## Match_id, Team1_id, Team2_id, Venue, City, Toss, Elected_to, Win_team, loser, Date, Win_by_runs, Win_by_wickets
        record =   "" + str(match_id) + ", " + str(team1) + "," + str(team2) + "," + \
                str(venue) + "," + str(city) + "," + str(toss) + "," + str(elected_to) \
                + "," + str(win_team) + "," + str(loser_team) + "," + str(date) + "," +\
                str(win_rums) + "," + str(win_wickets) + "\n"

#        print record
        csv.write(record)

    except:
        #print("Sorry" + str(i))
        e = sys.exc_info()[0]
        print(e)
        errors.append(str(i))

print("---Summary---")
print("Errors: " + len(errors))
csv.close()
