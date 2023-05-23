import re
import sys
import timeit


def is_valid(passport):
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return required_fields.issubset(set(passport.keys()))


def parse_passport(data):
    return {k: v for k, v in re.findall(r'(\S+):(\S+)', data)}


def single_threaded(data):
    passports = [parse_passport(passport) for passport in data]
    return sum(is_valid(passport) for passport in passports)


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        data = f.read().split('\n\n')
        start = timeit.default_timer()
        print(single_threaded(data))
        end = timeit.default_timer()
        print(f"Single-threaded execution time: {end - start}")
