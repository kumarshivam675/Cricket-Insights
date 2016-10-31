import yaml
import csv
from os import listdir


def get_filenames():
    return listdir('../../data')


def write_to_csv(player_out, other_player, batting_team, oppenent_team):
    hello = [[player_out, other_player, batting_team, oppenent_team]]

    with open('../../final data generated/number_runouts.csv', 'a') as testfile:     # append it data to the csv file
        csv_writer = csv.writer(testfile)
        csv_writer.writerow(hello[0])


def extract_info():
    for file in get_filenames():
        print file
        f = open('../../data/' + file)
        match = yaml.safe_load(f)
        innings_list = ["1st innings", "2nd innings"]
        team_list = match["info"]["teams"]
        for innings in innings_list:
            try:
                batting_team = match['innings'][innings_list.index(innings)][innings]["team"]
                bowling_team = team_list[abs(1 - team_list.index(batting_team))]
                for ball in match['innings'][innings_list.index(innings)][innings]["deliveries"]:
                    for key in ball:
                        if "wicket" in ball[key]:
                            if ball[key]["wicket"]["kind"] == "run out":
                                players = [ball[key]["batsman"], ball[key]["non_striker"]]
                                player_out = ball[key]["wicket"]["player_out"]
                                # print ball[key]
                                players.pop(players.index(player_out))
                                # print player_out, players[0]
                                # print batting_team, bowling_team
                                write_to_csv(player_out, players[0], batting_team, bowling_team)
            except:
                print "error in file"

extract_info()
