import csv


def save(batsman, bowler, zero, one, two, three, four, five, six, wicket):

    hello = [[batsman, bowler, zero, one, two, three, four, five, six, wicket]]

    with open('batsman_vs_bowler_total.csv', 'a') as testfile:     # append it data to the csv file
        csv_writer = csv.writer(testfile)
        csv_writer.writerow(hello[0])
