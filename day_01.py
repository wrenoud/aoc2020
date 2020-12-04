import util


def findSum(target, collection):
    for v in collection:
        if target - v in data:
            return (v, target - v)
    return (None, None)


def part1(data):
    first, second = findSum(2020, data)
    util.Answer(1, first * second)


def part2(data):
    for first in data:
        second, third = findSum(2020 - first, data)
        if second is not None:
            util.Answer(2, first * second * third)
            break


if __name__ == "__main__":
    data = set(int(v) for v in util.ReadPuzzle())
    part1(data)
    part2(data)
