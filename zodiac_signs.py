PLAYERS="c:/Users/semah/Desktop/polito year 1/sportivi.csv"
SIGNS="c:/Users/semah/Desktop/polito year 1/zodiaco.csv"
import csv
def get_mmdd(date_str):
    parts=date_str.split("/")
    day=parts[0].strip().zfill(2)
    month= parts[1].strip().zfill(2)
    return f"{month}{day}"
def read_players(filename):
    players=list()
    try:
        with open(filename, encoding="utf-8") as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                players.append({"goals":int(row[1]),"mmdd":get_mmdd(row[3])})
    except OSError as problem:
        print(problem)
        exit(1)
    return players

def read_signs(filename):
    signs=list()
    try:
        with open(filename, encoding="utf-8") as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                signs.append({"name":row[0],"start":get_mmdd(row[1]),"end":get_mmdd(row[2]),"total_goals":0})
            
        
    except OSError as problem:
        print(problem)
        exit(1)
    return signs

def main():
    players=read_players(PLAYERS)
    signs=read_signs(SIGNS)
    for p in players:
        p_date=p['mmdd']
        for s in signs:
            if s['start'] > s['end']:
                if p_date >= s['start'] or p_date <= s['end']:
                    s['total_goals']+=p['goals']
                    break
            elif s['start']<=p_date<=s['end']:
                s['total_goals']+=p['goals']
                break
    signs.sort(key=lambda x:x['total_goals'], reverse=True)
    max_goals=signs[0]['total_goals']

    for s in signs:
        num_asterics=int((s['total_goals']/max_goals)*50)
        bar="*"* num_asterics
        print(f"{s['name']}  {s['total_goals']} {bar}")

if __name__=="__main__":
    main()