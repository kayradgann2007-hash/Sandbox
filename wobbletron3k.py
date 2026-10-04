FILE="c:/Users/semah/Desktop/polito year 1/reports_long.dat"
OUTPUTFILE="c:/Users/semah/Desktop/polito year 1/correct-reports.dat"
def read_reports(filename):
    reports=list()
    try:
        with open(filename) as file:
            for line in file:
                rep= list()
                for level in line.split():
                    rep.append(int(level))
                reports.append(rep)
        return reports
    except OSError as problem:
        print(problem)
        exit(1)

def write_reports(reports,filename):
    try:
        with open(filename,"w") as file:
            for rep in reports:
                for level in rep[:-1]:
                    file.write(f"{level} ")
                file.write(f"{rep[-1]}\n")
    except OSError as problem:
        print(problem)
        exit(1)

def check_report_safety(report):
    if report != sorted(report) and report != sorted(report, reverse=True):
        return False
    for e1,e2 in zip(report,report[1:]):
        if abs(e1-e2)<1 or abs(e1-e2)>3:
            return False
    return True
def main():
    all_reports=read_reports(FILE)
    correct_reports=list()
    for report in all_reports:
        if check_report_safety(report):
            correct_reports.append(report)
    write_reports(correct_reports,OUTPUTFILE)
    print(f"Read {len(all_reports)} reports: {len(correct_reports)/len(all_reports):.2%} correct")


if __name__=="__main__":
    main()
