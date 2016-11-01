import pandas as pd

csv_file = "C:/Users/siddartha/Desktop/sid/data_analatics/Cricket-Insights/final data generated/team_summary.csv"
out_file = "C:/Users/siddartha/Desktop/sid/data_analatics/Cricket-Insights/final data generated/venue_innings.csv"

team_summary = pd.read_csv(csv_file)

#team_summary["year"] = team_summary.Date
team_summary['Year'] = team_summary['Date'].str[:4]


grouped =  team_summary.groupby(['Year', 'Venue'], as_index=True)
clms = ['Year', 'Stadium', 'Batting_first_wins', 'Batting_second_wins']
final = pd.DataFrame(columns=clms)

for g, grp in grouped:
    tmp = grp[['Venue', 'Year', 'Win_team', 'Toss', 'Elected_to']]
    #Year, Stadium, Batting_fist_wins, Batting Second Wins,
    year = g[0]
    stadium = g[1]
    batting_first_wins = 0
    batting_second_wins = 0

    for index, rows in tmp.iterrows():
        if(rows['Win_team'] == rows['Toss'] and rows['Elected_to'] == 'bat'):
            batting_first_wins += 1
        elif(rows['Win_team'] != rows['Toss'] and rows['Elected_to'] == 'bat'):
            batting_second_wins += 1
        elif(rows['Win_team'] == rows['Toss'] and rows['Elected_to'] == 'field'):
            batting_second_wins += 1
        elif(rows['Win_team'] != rows['Toss'] and rows['Elected_to'] == 'field'):
            batting_first_wins += 1

    final_row = pd.DataFrame([[year, stadium, batting_first_wins, batting_second_wins]], columns = ['Year', 'Stadium', 'Batting_first_wins', 'Batting_second_wins'])

    final = final.append(final_row)


final.to_csv(out_file, sep="," , columns=clms)


