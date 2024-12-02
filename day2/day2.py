# day2.py
# Yes, this is a mess.
# Will I tidy it? No. I want this to be a warning to all newbies coming in to AoC - DO NOT
# get excited about optimising part 1, because you can paint yourself into a corner and end up
# having to re-write most of it because you made it completely inextensible.
# And this doesn't work either


def main():
    reports = readInputFromFile()
    safeReports = 0
    unsafeReports = 0
    for report in reports:
        if isReportValid(report):
            safeReports += 1 
        else:
            if canReportBeCleaned(report):
                safeReports += 1
            else:
                unsafeReports += 1
    
    print(f'{safeReports} reports are safe') # ANS1: 516, ANS2: 
    print(f'{unsafeReports} reports are unsafe') # ANS1: 484, ANS2: 


def isReportValid(report: list) -> bool:
    return isReportInSequentialOrder(report) and isReportFormatted(report)


def isReportInSequentialOrder(report: list) -> bool:
    ascendingOrder = all(report[i] <= report[i+1] for i in range(len(report) - 1))
    descendingOrder = all(report[i] >= report[i+1] for i in range(len(report) - 1))
    return True if (ascendingOrder or descendingOrder) else False


def isReportFormatted(report: list) -> bool:
    return all(abs(report[i] - report[i+1]) in range(1, 4) for i in range(len(report) - 1))


def canReportBeCleaned(report: list) -> bool:
    # First check if the report is formatted correctly (increments/decrements) 
    problemIndices = []
    for i in range(len(report) - 1):
        if not (abs(report[i] - report[i+1]) in range(1, 4)):
            problemIndices.append(i)
    
    # print(problemIndices)

    if len(problemIndices) > 1:
        return False
    elif len(problemIndices) == 1:
        del(report[problemIndices[0]])
        return True if isReportValid(report) else False
    else:
        # Problem must be with the sequence - attempt to assess and fix this
        problemIndices = []
        if not all(report[i] <= report[i+1] for i in range(len(report) - 1)):
            for i in range(len(report) - 1):
                if not report[i] <= report[i+1]:
                    problemIndices.append(i)

        if len(problemIndices) == len(report):
            problemIndices.clear()
            if not all(report[i] >= report[i+1] for i in range(len(report) - 1)):
                for i in range(len(report) - 1):
                    if not report[i] <= report[i+1]:
                        problemIndices.append(i)

                if len(problemIndices) > 1:
                    return False
                elif len(problemIndices) == 1:
                    del(report[problemIndices[0]])
                    return True if isReportValid(report) else False

        elif len(problemIndices) > 1:
            return False
        elif len(problemIndices) == 1:
            del(report[problemIndices[0]])
            return True if isReportValid(report) else False   



def readInputFromFile() -> list: 
    reportList = []
    with open("./day2/input.txt", "r") as f:
        input = f.read()
        rawReportList = input.split("\n")
        for report in rawReportList:
            formattedReport = [int(level) for level in report.split(" ")]
            reportList.append(formattedReport)

    return reportList


if __name__ == "__main__":
    main()
