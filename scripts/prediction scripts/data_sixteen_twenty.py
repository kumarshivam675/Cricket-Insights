from os import listdir
import yaml
import csv


def write_to_csv(file, venue, team1, team2, MR, MRN, MW, OR, ORN, OW, win):

    hello = [[file, venue, team1, team2, MR, MRN, MW, OR, ORN, OW, win]]

    with open('sixteen_twenty_overs.csv', 'a') as testfile:     # append it data to the csv file
        csv_writer = csv.writer(testfile)
        csv_writer.writerow(hello[0])


def extract_data():
    innings_list = ["1st innings", "2nd innings"]
    count = 0
    write_to_csv("file", "venue", "team1", "team2", "MR", "MRN", "MW", "OR", "ORN", "OW", "win")
    for file in listdir('../../data'):
        first_innings_stat = []
        second_innings_stat = []
        count += 1
        flag = 0
        print file
        f = open('../../data/' + file)
        match = yaml.safe_load(f)
        if "city" in match['info']:
            venue = match['info']['city']
        else:
            venue = "neutral"

        for innings in innings_list:
            runs = 0
            wicket = 0
            ball_count = 0
            try:
                for ball in match['innings'][innings_list.index(innings)][innings]["deliveries"]:
                    for key in ball:
                        if float(key) >= 15.0 and float(key) < 20:
                            ball_count += 1
                            runs += ball[key]["runs"]["total"]
                            if "wicket" in ball[key]:
                                wicket += 1
                if ball_count > 30:     # to handle the case when less than six overs are bowled
                    balls = 30
                else:
                    balls = ball_count

                runrate = float(runs)/float(balls)*6.0

                if innings == "1st innings":
                    team_1 = match['innings'][0]["1st innings"]['team']
                    first_innings_stat.append(runs)
                    first_innings_stat.append(runrate)
                    first_innings_stat.append(wicket)

                else:
                    team_2 = match['innings'][1]["2nd innings"]['team']
                    second_innings_stat.append(runs)
                    second_innings_stat.append(runrate)
                    second_innings_stat.append(wicket)
                    # print second_innings_stat
            except:
                flag = 1

        if flag != 1:
            if "winner" in match['info']['outcome']:
                winner = match['info']['outcome']['winner']
            else:
                winner = "tie"

            write_to_csv(file.split(".")[0], venue, team_1, team_2, first_innings_stat[0], first_innings_stat[1], first_innings_stat[2],
                         second_innings_stat[0], second_innings_stat[1], second_innings_stat[2], winner)


extract_data()
