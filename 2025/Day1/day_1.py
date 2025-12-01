def parse_line(line: str):
    line = line.strip()
    return [line[0], int(line[1 : len(line)])]


def main():
    dial = 50
    res = 0
    with open("/home/thibault/Code/Advent-Of-Code/2025/Day1/input.txt", "r") as file:
        for line in file:
            direction, step = parse_line(line)

            if direction == "R":
                dial = dial + step
            elif direction == "L":
                dial = dial - step

            dial = dial % 100

            if dial == 0:
                res += 1

    print(res)


if __name__ == "__main__":
    main()
