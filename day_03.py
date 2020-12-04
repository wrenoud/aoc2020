import util
from lib import Coord


def traverse(hill, slope):
    position = Coord(0, 0)
    encounters = 0
    while position.y < len(hill):
        line = hill[position.y]
        encounters += line[position.x % len(line)] == "#"
        position += slope
    return encounters


def part1(data):
    util.Answer(1, traverse(data, Coord(3, 1)))


def part2(data):
    util.Answer(
        2,
        traverse(data, Coord(1, 1))
        * traverse(data, Coord(3, 1))
        * traverse(data, Coord(5, 1))
        * traverse(data, Coord(7, 1))
        * traverse(data, Coord(1, 2)),
    )


if __name__ == "__main__":

    data = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ]

    assert traverse(data, Coord(3, 1)) == 7

    data = util.ReadPuzzle()

    part1(data)
    part2(data)
