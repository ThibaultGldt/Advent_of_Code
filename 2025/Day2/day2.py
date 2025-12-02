def parse_input(input):
    return [tuple(map(int, pair.split("-"))) for pair in input.split(",")]


def build_range(boundaries):
    start, end = boundaries
    r = list(range(start, end + 1))
    return r


def find_invalid(range):
    sum = 0
    for i in range:
        s = str(i)
        s1, s2 = s[: len(s) // 2], s[len(s) // 2 :]
        if s1 == s2:
            sum += i
    return sum


def main():
    sum = 0
    with open("Day2/input.txt", "r") as f:
        input = f.read()
        pairs = parse_input(input)
        for pair in pairs:
            range = build_range(pair)
            sum += find_invalid(range)
    print(sum)


if __name__ == "__main__":
    main()
