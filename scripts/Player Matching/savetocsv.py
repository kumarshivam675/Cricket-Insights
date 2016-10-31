import csv


def save(player_dataset, player_scraped1, player_scraped2, player_scraped3):

    hello = [[player_dataset, player_scraped1, player_scraped2, player_scraped3]]

    with open('player_dataset_vs_player_scraped.csv', 'a') as testfile:     # append it data to the csv file
        csv_writer = csv.writer(testfile)
        csv_writer.writerow(hello[0])
