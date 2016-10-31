import csv

import savetocsv


def create_player_list():
    player_dataset = []
    player_scrapped = []
    with open('scorecard.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            player_dataset.append(row[0])

    with open('playerDimension.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            player_scrapped.append(row[0])

    return player_dataset, player_scrapped


def extract_dataset_player_name(player):
    player_name = player.split(" ")
    remove = []
    for name in player_name:
        if len(name) <= 3:
            remove.append(player_name.index(name))

    remove.sort(reverse=True)
    for index in remove:
        player_name.pop(index)
    return player_name, player


def export_to_csv(map):
    match = ["", "", ""]
    print len(map)
    for key in map:
        match = ["", "", ""]
        print key
        player_db = key
        for i in range(0, len(map[key])):
            match[i] = map[key][i]
            if i >= 2:
                break

        savetocsv.save(player_db, match[0], match[1], match[2])


def match_player():
    map = {}
    count = 0
    player_dataset, player_scrapped = create_player_list()
    for player_db in player_dataset:
        count += 1
        try:
            player_name_split, player_name = extract_dataset_player_name(player_db)
            # print player_name

            if len(player_name_split) == 1:
                for player_srp in player_scrapped:
                    if player_name_split[0] in player_srp:
                        if player_name in map:
                            map[player_name].append(player_srp)
                        else:
                            map[player_name] = [player_srp]

            else:
                common_list = []
                for name in player_name_split:
                    temp = []
                    for player_srp in player_scrapped:
                        if name in player_srp:
                            temp.append(player_srp)
                    common_list.append(temp)

                final = common_list[0]
                for i in range(1, len(common_list)):
                    final = list(set(final) & set(common_list[i]))

                for player in final:
                    if player_name in map:
                        map[player_name].append(player)
                    else:
                        map[player_name] = [player]

        except:
            print "error in matching"

    print map
    export_to_csv(map)
match_player()