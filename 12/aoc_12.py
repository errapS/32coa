from itertools import product
import re
import numpy as np
from tqdm import tqdm
from functools import cache


def generate_pattern(spring: list) -> str:
    last = len(spring)
    pattern = ''
    for i in range(last):
        if i == 0:
            pattern += f"0*1{{{spring[i]}}}0+"
        elif i == last - 1:
            pattern += f"1{{{spring[i]}}}0*"
        else:
            pattern += f"1{{{spring[i]}}}0+"

    return pattern


def generate_combinations(list, length):
    pattern = re.compile(generate_pattern(list))

    re_combinations = []
    combinations = product('01', repeat=length)

    for c in combinations:
        c_str = ''.join(c)
        if pattern.fullmatch(c_str):
            re_combinations.append(c_str)
    
    return re_combinations


def is_valid_combination(binary_string, allowed_ones, none_zeros):
    for idx, value in enumerate(binary_string):
        if value == '1' and allowed_ones[idx] == 0:
            return False
        if value == '0' and none_zeros[idx] == 1:
            return False
    return True

def process_line(line):
    condition_record, spring = line.split()
    spring = [int(i) for i in spring.split(',')]
    condition = np.array([list(condition_record.strip())])

    spring_schema = np.all((condition == '#') | (condition == '?'), axis=0).astype(int)
    broken = np.all((condition == '#'), axis=0).astype(int)

    combinations = generate_combinations(spring, len(spring_schema))
    valid_combinations = [c for c in combinations if is_valid_combination(c, spring_schema, broken)]

    return len(valid_combinations)


@cache
def combinations(schema, springs, result=0):
    if not springs:
        return '#' not in schema
    
    current, springs = springs[0], springs[1:]
    for i in range(len(schema) - sum(springs) - len(springs) - current + 1):
        if "#" in schema[:i]:
            break
        if (nxt := i + current) <= len(schema) and '.' not in schema[i : nxt] and schema[nxt : nxt + 1] != "#":
            result += combinations(schema[nxt + 1:], springs)
    return result


with open('12/test.txt', 'r') as f:
    lines = f.readlines()

    res1 = 0
    for line in tqdm(lines, desc="Processing lines", unit="line"):
        res1 += process_line(line)


with open('12/input.txt', 'r') as f:
    lines = [l.split() for l in f.readlines()]
    
    res2 = 0
    for i, (spring_schema, springs) in enumerate(lines):
        springs = tuple(map(int, springs.split(",")))
        res2 += combinations("?".join([spring_schema] * 5), springs * 5)

print('ANSWER PART A', res1)
print('ANSWER PART B', res2)  

