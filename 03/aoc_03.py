import re

def find_indexes(input_string):
    numbers = re.finditer(r'\b\d+\b', input_string)
    ind_num = [(match.start() - 1, match.end()) for match in numbers]
    ind_sym = [index for index, char in enumerate(input_string) if char in "!@#$%^&*()-=_+[]{}|;:'\",<>?/\\`~"]

    return ind_sym, ind_num

def find_adjecent(line, num_range, sym_indexes):
    res = []

    for num in num_range:
        if any(num[0] <= sym <= num[1] for sym in sym_indexes):
            res.append(int(line[num[0] + 1:num[-1]]))

    return res

lines = [line for line in open('03/input.txt').readlines()]

lines_indexes = [find_indexes(line) for line in lines]
symbol_indexes, number_indexes = zip(*lines_indexes)

r = []
for i, symind in enumerate(symbol_indexes):
    if i == 0:
        r.append(find_adjecent(lines[i], number_indexes[i], symind))
        r.append(find_adjecent(lines[i+1], number_indexes[i+1], symind))
    elif i == len(lines) - 1:
        r.append(find_adjecent(lines[i], number_indexes[i], symind))
        r.append(find_adjecent(lines[i-1], number_indexes[i-1], symind))
    else:
        for j in range(0,3):
            r.append(find_adjecent(lines[i-1+j], number_indexes[i-1+j], symind))

print('ANSWER PART A: ', sum([sum(k) for k in r]))



def find_indexes_gears(row_id, input_string):
    numbers = re.finditer(r'\b\d+\b', input_string)
    ind_num = {tuple((row_id, match.start(), match.end()-1)): int(match.group()) for match in numbers}
    ind_sym = {tuple((row_id, index)): [] for index, char in enumerate(input_string) if char == "*"}
    
    return ind_sym, ind_num


lines = open('03/input.txt').readlines()
lines_indexes = [find_indexes_gears(i, line) for i, line in enumerate(open('03/input.txt').readlines())]
symbol_indexes, number_indexes = zip(*lines_indexes)

for symbol in symbol_indexes:
    for row, idx in symbol:
        lr = -1
        ur = 2
        if row == 0:
            lr = 0
        elif row == len(lines)-1:
            ur = 1

        for row_i in range(lr,ur):
            number_row = lines[row+row_i]
            last_append_row = 0
            for col_j in range(-1,2):
                hit = idx + col_j
                char = number_row[hit]

                if char.isdigit():
                    left = hit
                    while char.isdigit():
                        left -= 1
                        char = number_row[left]

                    right = hit
                    char = number_row[right]
                    while char.isdigit():
                        right += 1
                        char = number_row[right]

                    gear = number_indexes[row+row_i][(row+row_i, left+1, right-1)]

                   
                    if gear not in symbol_indexes[row][(row, idx)]:
                        symbol_indexes[row][(row, idx)].append(gear)
                        last_append_row = row+row_i
                    elif gear in symbol_indexes[row][(row, idx)] and row+row_i != last_append_row:
                        symbol_indexes[row][(row, idx)].append(gear)
                        last_append_row = row+row_i


res = 0
for sym in symbol_indexes:
    for pair in sym.values():
        if len(pair) == 2:
            res += pair[0] * pair[1]

print('ANSWER PART B: ', res)





