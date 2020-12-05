import io
import re

#   byr (Birth Year) - four digits; at least 1920 and at most 2002.
#   iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#   eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#   hgt (Height) - a number followed by either cm or in:
#       If cm, the number must be at least 150 and at most 193.
#       If in, the number must be at least 59 and at most 76.
#   hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#   ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#   pid (Passport ID) - a nine-digit number, including leading zeroes.
#   cid (Country ID) - ignored, missing or not.


def byr(s):
    i = int(s)
    return i >= 1920 and i <= 2002


def iyr(s):
    i = int(s)
    return i >= 2010 and i <= 2020


def eyr(s):
    i = int(s)
    return i >= 2020 and i <= 2030


def hgt(s):
    if s.endswith('cm'):
        i = int(s[0:-2])
        return i >= 150 and i <= 193

    if s.endswith('in'):
        i = int(s[0:-2])
        return i >= 59 and i <= 76
    return False


pattern = re.compile("[a-f0-9]+")


def hcl(s):
    if(s[0] != '#'):
        return False

    return pattern.fullmatch(s[1:]) != None


col = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def ecl(s):
    return s in col


def pid(s):
    return s.isdigit() and len(s) == 9


def cid(s):
    return True


dict = {
    'byr': byr,
    'iyr': iyr,
    'eyr': eyr,
    'hgt': hgt,
    'hcl': hcl,
    'ecl': ecl,
    'pid': pid,
    'cid': cid
}


def validPass(p):
    def d(s):
        return False
    n = 0
    fields = p.replace('\n', ' ').split(' ')

    for f in fields:
        s = f.split(':')

        fn = dict.get(s[0], d)

        if fn(s[1]) == False:
            return False
        if s[0] != 'cid':
            n += 1
    return n == 7


with open("input.txt", "r", encoding="utf-8") as g:
    data = g.read().split('\n\n')

total = 0

for p in data:
    if validPass(p):
        total += 1


print(total)
