BOWLING="c:/Users/semah/Desktop/polito year 1/bowling.txt"

def readfile(filename):
    try:
        player_stats=list()
        with open(filename) as file:
            for line in file:
                player_stats.append(line.rstrip().split(";"))
    except OSError as problem:
        print(problem)
        exit(1)
    return player_stats

def all_players(player_stats):
    players=list()
    for row in (player_stats):
        players.append( row[0]+" "+row[1])
    return players

def summary(player_stats):
    points=list()
    for row in player_stats:
        total=0
        for i in row[2:]:
            i=int(i)
            total+=i
        points.append(total)
    return points



def main():
    player_stats=readfile(BOWLING)
    players=all_players(player_stats)
    points=summary(player_stats)
    all_info=dict()
    for i in range(len(player_stats)):
        all_info[players[i]]=points[i]
    sorted_board=dict(sorted(all_info.items(),key=lambda x:x[1], reverse=True))
    for k,v in sorted_board.items():
        print(f"{k}: {v}")
    all_pins=list()
    no_pins=list()
    for row in (player_stats[2:]):
        a=0
        b=0
        for seq in row:
            if seq=="10":
                a+=1
            elif seq=="0":
                b+=1
        all_pins.append(a)
        no_pins.append(b)
    index_max=all_pins.index(max(all_pins))
    print(f"Player with most strikes: {players[index_max]} with {all_pins[index_max]} strikes")
    index_min=no_pins.index(max(no_pins))
    print(f"Player with most gutter balls: {players[index_min]} with {no_pins[index_min]} gutter balls")

    




if __name__=="__main__":
    main()