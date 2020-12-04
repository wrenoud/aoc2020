import util
import re


def isSimpleValid(credential):
    return len(credential.keys()) == 8 or (
        len(credential.keys()) == 7 and "cid" not in credential
    )


def byr(v):
    return int(v) >= 1920 and int(v) <= 2002


assert not byr("1919")
assert byr("1920")
assert byr("2002")
assert not byr("2003")


def iyr(v):
    return int(v) >= 2010 and int(v) <= 2020


assert iyr("2010")
assert iyr("2020")
assert not iyr("2021")
assert not iyr("2009")


def eyr(v):
    return int(v) >= 2020 and int(v) <= 2030


assert eyr("2020")
assert eyr("2030")
assert not eyr("2031")
assert not eyr("2019")


def hgt(v):
    match = re.fullmatch("(?P<height>[0-9]+)(?P<unit>cm|in)", v)
    if match is None:
        return False

    height = int(match["height"])
    if match["unit"] == "cm":
        return height >= 150 and height <= 193
    if match["unit"] == "in":
        return height >= 59 and height <= 76
    else:
        return False


assert not hgt("149cm")
assert hgt("150cm")
assert hgt("193cm")
assert not hgt("194cm")
assert not hgt("58in")
assert hgt("59in")
assert hgt("76in")
assert not hgt("77in")
assert not hgt("190in")
assert not hgt("190")


def hcl(v):
    return re.fullmatch("#[0-9a-f]{6}", v) is not None


assert hcl("#ffffff")
assert not hcl("#123abz")
assert not hcl("#fffff")


def ecl(v):
    return v in [
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth",
    ]


assert ecl("oth")
assert not ecl("wat")


def pid(v):
    return re.fullmatch("[0-9]{9}", v) is not None


assert pid("012345678")
assert not pid("01234567")
assert not pid("0123456789")

tests = {
    "byr": byr,
    "iyr": iyr,
    "eyr": eyr,
    "hgt": hgt,
    "hcl": hcl,
    "ecl": ecl,
    "pid": pid,
}


def isValid(credential):
    if not isSimpleValid(credential):
        return False

    for key, test in tests.items():
        if not test(credential[key]):
            return False

    return True


def part1(data):
    util.Answer(1, sum(isSimpleValid(credential) for credential in data))


def part2(data):
    util.Answer(2, sum(isValid(credential) for credential in data))


def ConvertCredentials(data):
    credentials = [{}]
    for line in data:
        if line == "":
            credentials.append({})
            continue
        for key, value in [v.split(":") for v in line.split(" ")]:
            credentials[-1][key] = value
    return credentials


if __name__ == "__main__":

    data = [
        "eyr:1972 cid:100",
        "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
        "",
        "iyr:2019",
        "hcl:#602927 eyr:1967 hgt:170cm",
        "ecl:grn pid:012533040 byr:1946",
        "",
        "hcl:dab227 iyr:2012",
        "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
        "",
        "hgt:59cm ecl:zzz",
        "eyr:2038 hcl:74454a iyr:2023",
        "pid:3556412378 byr:2007",
        "",
        "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
        "hcl:#623a2f",
        "",
        "eyr:2029 ecl:blu cid:129 byr:1989",
        "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
        "",
        "hcl:#888785",
        "hgt:164cm byr:2001 iyr:2015 cid:88",
        "pid:545766238 ecl:hzl",
        "eyr:2022",
        "",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
    ]

    credentials = ConvertCredentials(data)
    assert len(credentials) == 8
    assert sum(isValid(credential) for credential in credentials) == 4

    data = util.ReadPuzzle()
    credentials = ConvertCredentials(data)
    part1(credentials)
    part2(credentials)
