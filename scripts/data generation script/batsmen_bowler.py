# Generates data of batsmen vs bowler vs No. of zeors, one, two.... siz scored, no of wickets taken

from os import listdir
import yaml
import csv


def get_filenames():
    return listdir('../../data')


def structure_data_dictionary(data):
    for key in data:
        batsman = key
        for key2 in data[key]:
            bowler = key2
            zero = data[key][key2][0]
            one = data[key][key2][1]
            two = data[key][key2][2]
            three = data[key][key2][3]
            four = data[key][key2][4]
            five = data[key][key2][5]
            six = data[key][key2][6]
            wicket = data[key][key2][7]

            hello = [[batsman, bowler, zero, one, two, three, four, five, six, wicket]]

            with open('batsman_vs_bowler_total.csv', 'a') as testfile:     # append it data to the csv file
                csv_writer = csv.writer(testfile)
                csv_writer.writerow(hello[0])


def extract_info():
    data = {}
    count = 0
    innings_list = ["1st innings", "2nd innings"]
    for file in get_filenames():
        print file, count
        count += 1
        try:
            f = open('./data/' + file)
            match = yaml.safe_load(f)
            for innings in innings_list:
                for ball in match['innings'][innings_list.index(innings)][innings]["deliveries"]:
                    for key in ball:
                        runs = ball[key]["runs"]["batsman"]
                        if ball[key]["batsman"] in data:
                            if ball[key]["bowler"] not in data[ball[key]["batsman"]]:
                                data[ball[key]["batsman"]][ball[key]["bowler"]] = [0, 0, 0, 0, 0, 0, 0, 0]

                            if "wicket" in ball[key]:
                                    data[ball[key]["batsman"]][ball[key]["bowler"]][7] += 1
                            else:
                                data[ball[key]["batsman"]][ball[key]["bowler"]][runs] += 1

                        else:
                            data[ball[key]["batsman"]] = {}
                            data[ball[key]["batsman"]][ball[key]["bowler"]] = [0, 0, 0, 0, 0, 0, 0, 0]

                            if "wicket" in ball[key]:
                                    data[ball[key]["batsman"]][ball[key]["bowler"]][7] += 1
                            else:
                                data[ball[key]["batsman"]][ball[key]["bowler"]][runs] += 1
            f.close()

        except:
            print "error in file"

    structure_data_dictionary(data)

extract_info()