FILE="c:/Users/semah/Desktop/polito year 1/expressions_long.dat"

def readfile(filename):
    
    expressions=list()
    try:
        with open(filename) as file:
            for line in file:
                part_1,part_2=line.split(":")
                num=list()
                for i in part_1.split():
                    num.append(int(i))
                calcs=part_2.split()
                expressions.append((num,calcs))


        return expressions
    except OSError as problem:
        print(problem)
        exit(1)

def operation(op,a,b):
    if op=="*":
        return a*b
    elif op=="-":
        return a-b
    elif op=="+":
        return a+b

def calculation(numbers,operations):
    numbers=numbers[::-1]
    for ops in operations:
        numbers.append(operation(ops,numbers.pop(),numbers.pop()))
    return numbers[0]




    
def main():
    for nums,ops in readfile(FILE):
        print(calculation(nums,ops))
    

if __name__=="__main__":
    main()

