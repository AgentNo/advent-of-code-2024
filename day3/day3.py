# day3.py
import re

def main():
    mulConditionalList = readInputFromFile()
    total = 0
    mulEnabledIndicator = True

    for mul in mulConditionalList:
        if mul == 'do()':
            mulEnabledIndicator = True
            pass
        elif mul == "don't()":
            mulEnabledIndicator = False
            pass
        else:
            if mulEnabledIndicator == True:
                numbers = re.findall(r'\d+,\d+', mul)[0].split(',')
                total += (int(numbers[0]) * int(numbers[1]))
    
    print(f'The total for all valid muls is {total}') # ANS1: 184576302, ANS2: 118173507


def readInputFromFile() -> list: 
    with open("./day3/input.txt", "r") as f:
        input = f.read()
        mulList = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input)
        # print(mulList)
        return mulList


if __name__ == "__main__":
    main()
