import util


class Seat(object):
    def __init__(self, seatcode):
        self.row = 0
        self.col = 0

        for i, v in enumerate(seatcode[:7]):
            if v == "B":
                self.row += 2 ** (6 - i)
        for i, v in enumerate(seatcode[7:]):
            if v == "R":
                self.col += 2 ** (2 - i)

    @property
    def id(self):
        return self.row * 8 + self.col

    def __str__(self):
        return f"{self.row} {self.col} ({self.id})"


assert Seat("FBFBBFFRLR").id == 357


def part1(data):
    util.Answer(1, max(Seat(code).id for code in data))


def part2(data):
    ids = list(Seat(code).id for code in data)
    ids.sort()
    for i,id in enumerate(ids[:-1]):
        if ids[i+1] - id == 2:
            util.Answer(2, id+1)
            break


if __name__ == "__main__":
    data = util.ReadPuzzle()
    part1(data)
    part2(data)
