import re
import concurrent.futures
import sys
import timeit


def is_valid(passport):
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return required_fields.issubset(set(passport.keys()))


def parse_passport(data):
    return {k: v for k, v in re.findall(r'(\S+):(\S+)', data)}


def multi_threaded(data):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        passports = list(executor.map(parse_passport, data))
        valid_passports = list(executor.map(is_valid, passports))
        return sum(valid_passports)


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        data = f.read().split('\n\n')
        start = timeit.default_timer()
        print(multi_threaded(data))
        end = timeit.default_timer()
        print(f"Multi-threaded execution time: {end - start}")
