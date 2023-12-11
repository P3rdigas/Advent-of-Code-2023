def main():
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

    print(sum)

if __name__ == "__main__":
    main()