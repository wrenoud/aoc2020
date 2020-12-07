import util


def GroupAnyYes(group):
    yeses = set()
    for person in group:
        yeses = yeses.union(set(c for c in person))
    return len(yeses)


def GroupAllYes(group):
    yeses = set(c for c in group[0])
    for person in group[1:]:
        yeses = yeses.intersection(set(c for c in person))
    return len(yeses)


def part1(groups):
    util.Answer(1, sum(GroupAnyYes(group) for group in groups))


def part2(groups):
    util.Answer(2, sum(GroupAllYes(group) for group in groups))


if __name__ == "__main__":
    data = [
        "abc",
        "",
        "a",
        "b",
        "c",
        "",
        "ab",
        "ac",
        "",
        "a",
        "a",
        "a",
        "a",
        "",
        "b",
    ]

    data = util.ReadPuzzle()

    groups = [[]]

    for line in data:
        if line == "":
            groups.append([])
        else:
            groups[-1].append(line)

    part1(groups)
    part2(groups)
