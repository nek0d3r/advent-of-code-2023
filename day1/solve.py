def part1(filename):
    sum = 0
    with open(filename) as f:
        for line in f.readlines():
            left = 0
            right = len(line) - 1
            leftChar = ""
            rightChar = ""
            while leftChar == "" or rightChar == "":
                if line[left].isdigit() and leftChar == "":
                    leftChar = line[left]
                if line[right].isdigit() and rightChar == "":
                    rightChar = line[right]
                left += 1
                right -= 1
            num = int(leftChar + rightChar)
            print(f"Line: {line.strip()}\tCalibration value: {leftChar} + {rightChar} = {num}")
            sum += num
    print(f"Calibration value sum: {sum}")

def part2(filename):
    sum = 0
    digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    with open(filename) as f:
        for line in f.readlines():
            left = 0
            right = len(line) - 1
            leftChar = ""
            rightChar = ""
            leftWord = ""
            rightWord = ""
            while leftChar == "" or rightChar == "":
                if line[left].isdigit() and leftChar == "":
                    leftChar = line[left]
                if line[right].isdigit() and rightChar == "":
                    rightChar = line[right]
                leftWord += line[left]
                rightWord = line[right] + rightWord
                for digit in digits.keys():
                    if leftWord.find(digit) > -1 and leftChar == "":
                        leftChar = digits[digit]
                    if rightWord.find(digit) > -1 and rightChar == "":
                        rightChar = digits[digit]
                left += 1
                right -= 1
            num = int(leftChar + rightChar)
            print(f"Line: {line.strip()}\tCalibration value: {leftChar} + {rightChar} = {num}")
            sum += num
    print(f"Calibration value sum: {sum}")

part2("input.txt")