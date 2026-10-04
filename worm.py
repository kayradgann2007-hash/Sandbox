FILE="c:/Users/semah/Desktop/polito year 1/seq-long.txt"



def readfile(filename):
    list=[]
    try:
        with open(filename,"r") as f:
            for line in f:
                    
                sublist=line.split()
                list.append(sublist)
            
                
                
    except OSError as problem:
        print(problem)
        exit(1)   
    return list

def main():
    list= readfile(FILE)
    dict={}
    word_1=input(str("Select your first word.  "))
    word_2=input(str("Select your second word.  "))
    for seq,sublist in enumerate(list):
        
        if word_1 in sublist and word_2 in sublist:
            pos_1=-1
            for i in range(len(sublist)):
                if word_1==sublist[i]:
                    pos_1=i
                    break
            pos_2=-1
            for i in range(len(sublist)):
                if word_2==sublist[i]:
                    pos_2=i
                    break
                dist=abs((pos_2)-(pos_1))
            dict[seq+1]= dist
    if dict:
        best_seq=min(dict,key=dict.get)
        min_val=dict[best_seq]
        print(f"Min distance: sequence {best_seq} (distance={min_val})")




if __name__=="__main__":
    main()

