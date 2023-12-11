def main():
    # Part one
    sum = 0
    first = None
    last = None

    f = open("input.txt", "r")
    lines = f.readlines()

    for line in lines:
        for c in line:
            if c.isdigit():
                if first is None :
                    first = c
                else:
                    last = c

        number = 0

        if first is not None and last is not None:
            number = str(first) + str(last)
            sum += int(number)
        elif first is not None :
            number = str(first) + str(first)
            sum += int(number)

        first = None
        last = None      

    print("Part one sum: ", sum)

    # Part two
    sum = 0
    first = None
    last = None

    numbersDic = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    f = open("input2.txt", "r")
    lines = f.readlines()

    for line in lines:
        new_str = ""
        for c in line:
            if c.isdigit():
                if first is None :
                    first = c
                else:
                    last = c
                new_str = ""
            else:
                new_str += c
            
                numbers = numbersDic.keys()

                for number in numbers:
                    if number in new_str:
                        if first is None :
                            first = numbersDic[number]
                        else:
                            last = numbersDic[number]
                        new_str = ""
                        new_str += c

        number = 0

        if first is not None and last is not None:
            number = str(first) + str(last)
            sum += int(number)
        elif first is not None :
            number = str(first) + str(first)
            sum += int(number)

        first = None
        last = None

    print("Part two sum: ", sum)

if __name__ == "__main__":
    main()