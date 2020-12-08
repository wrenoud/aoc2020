import util


class Instruction(object):
    def __init__(self, instruction):
        self.operation, self.argument = instruction.split(" ")
        self.argument = int(self.argument)

    def __str__(self):
        return f"{self.operation} {self.argument}"


class Console(object):
    def __init__(self, instructions):
        self.instructions = [Instruction(instruction) for instruction in instructions]
        self.accumulator = 0
        self.cursor = 0

    def exec(self):
        self.accumulator = 0
        self.cursor = 0

        while self.cursor < len(self.instructions):
            yield self.cursor

            instruction = self.current_instruction
            if instruction.operation == "acc":
                self.accumulator += instruction.argument
                self.cursor += 1
            elif instruction.operation == "jmp":
                self.cursor += instruction.argument
            elif instruction.operation == "nop":
                self.cursor += 1

    @property
    def current_instruction(self):
        return self.instructions[self.cursor]


def HasInfiniteLoop(console):
    visited = set()
    for cursor in console.exec():
        if cursor in visited:
            return True
        visited.add(cursor)
    return False


def part1(data):
    console = Console(data)
    HasInfiniteLoop(console)
    util.Answer(1, console.accumulator)


def part2(data):
    console = Console(data)
    for i, instruction in enumerate(console.instructions):
        if instruction.operation == "jmp":
            instruction.operation = "nop"
            if not HasInfiniteLoop(console):
                print(i, instruction)
                break
            instruction.operation = "jmp"
        elif instruction.operation == "nop":
            instruction.operation = "jmp"
            if not HasInfiniteLoop(console):
                print(i, instruction)
                break
            instruction.operation = "nop"

    util.Answer(2, console.accumulator)


if __name__ == "__main__":
    data = [
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",
        "acc +6",
    ]

    data = util.ReadPuzzle()

    part1(data)
    part2(data)
