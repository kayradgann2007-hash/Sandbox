CSV_FILE="c:/Users/semah/Desktop/polito year 1/player_stats.csv"
TEXT_FIELDS={"player", "position", "team"}
import csv


def read_player_stats(filename):
    players=list()
    try:    
        with open(filename,newline='',encoding="utf-8") as csvfile:
            reader=csv.DictReader(csvfile)
            for row in reader:
                for k,v in row.items():
                    if k not in TEXT_FIELDS:
                        row[k]=int(v)
                players.append(row)
    except OSError as problem:
        print(problem)
        exit(1)
    return players
 
def split_teams(players):
    teams= dict()
    for p in players:
        if p['team'] not in teams:
            teams[p['team']]=list()
        teams[p["team"]].append(dict(p))
    return teams

def calculate_efficienncies(players):
    for p in players:
        p['forward_efficiency'] = (p['goals'] + p['assists'] - p['offsides']) / p['minutes']
        if p['crosses'] == 0:
            t = 0
        else:
            t = p['assists'] / p['crosses']
        p['midfield_efficiency'] = (p['interceptions'] + p['ball_recoveries'] + t) / p['minutes']

def main():
    players=read_player_stats(CSV_FILE)
    calculate_efficienncies(players)
    

        
