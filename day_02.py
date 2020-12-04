import util


def testPolicy(min, max, letter, password):
    count = password.count(letter)
    return count >= min and count <= max


def testNewPolicy(min, max, letter, password):
    if len(password) < max:
        return False
    minl = password[min - 1]
    maxl = password[max - 1]
    return minl != maxl and (minl == letter or maxl == letter)


def part1(data):
    util.Answer(
        1,
        sum(
            testPolicy(min, max, letter, password)
            for min, max, letter, password in data
        ),
    )


def part2(data):
    util.Answer(
        2,
        sum(
            testNewPolicy(min, max, letter, password)
            for min, max, letter, password in data
        ),
    )


if __name__ == "__main__":
    data = []
    for rng, letter, password in [v.split(" ") for v in util.ReadPuzzle()]:
        min, max = rng.split("-")
        data.append((int(min), int(max), letter[0], password))
    part1(data)
    part2(data)
