import util
import re


class Bag(object):
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.contains = []

    def collect_parents(self):
        parents = set()
        for parent in self.parents:
            parents.add(parent.name)
            parents |= parent.collect_parents()
        return parents

    def count_children(self):
        count = 0
        for num, child in self.contains:
            count += num + num * child.count_children()

        return count

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def part1(data):
    bag = data["shiny gold"]
    util.Answer(1, len(bag.collect_parents()))


def part2(data):
    bag = data["shiny gold"]
    util.Answer(2, bag.count_children())


if __name__ == "__main__":

    data = [
        "light red bags contain 1 bright white bag, 2 muted yellow bags.",
        "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
        "bright white bags contain 1 shiny gold bag.",
        "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
        "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
        "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
        "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
        "faded blue bags contain no other bags.",
        "dotted black bags contain no other bags.",
    ]

    data = util.ReadPuzzle()

    bags = {}
    for line in data:
        name, contains = line.split(" bags contain ")
        if name not in bags:
            bags[name] = Bag(name)
        for bag in contains[:-1].split(", "):
            match = re.match("([0-9]+) (.*) bags?", bag)
            if match is not None:
                subname = match.group(2)
                if subname not in bags:
                    bags[subname] = Bag(subname)
                bags[subname].parents.append(bags[name])
                bags[name].contains.append((int(match.group(1)), bags[subname]))

    part1(bags)
    part2(bags)
