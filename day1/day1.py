# day1.py

def main():
    leftList, rightList = readAndFormatInput()
    distance = 0
    similarityScores = dict()
    for x in range(len(leftList)):
        distance += abs(leftList[x] - rightList[x])
        occurences = rightList.count(leftList[x])
        similarityScores.update({leftList[x]: occurences * leftList[x]})
    
    print(f"The total distance between lists is {distance}") # ANS: 1258579
    print(f"The total similarity score between lists is {sum(similarityScores.values())}") # ANS: 23981443


def readAndFormatInput() -> tuple: 
    leftList, rightList = [], []
    with open("./day1/input.txt", "r") as f:
        input = f.read()
        inputRowList = input.split("\n")
        for row in inputRowList:
            leftValue, rightValue = map(int, row.split(" " * 3))
            leftList.append(leftValue)
            rightList.append(rightValue)
        leftList.sort()
        rightList.sort()

    return leftList, rightList


if __name__ == "__main__":
    main()
