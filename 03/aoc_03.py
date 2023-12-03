import re

# def find_indexes(input_string):
#     numbers = re.finditer(r'\b\d+\b', input_string)
#     ind_num = [(match.start() - 1, match.end()) for match in numbers]
#     ind_sym = [index for index, char in enumerate(input_string) if char in "!@#$%^&*()-=_+[]{}|;:'\",<>?/\\`~"]

#     return ind_sym, ind_num

# def find_adjecent(line, num_range, sym_indexes):
#     res = []

#     for num in num_range:
#         if any(num[0] <= sym <= num[1] for sym in sym_indexes):
#             res.append(int(line[num[0] + 1:num[-1]]))

#     return res

# lines = [line for line in open('input.txt').readlines()]

# lines_indexes = [find_indexes(line) for line in lines]
# symbol_indexes, number_indexes = zip(*lines_indexes)

# r = []
# for i, symind in enumerate(symbol_indexes):
#     if i == 0:
#         r.append(find_adjecent(lines[i], number_indexes[i], symind))
#         r.append(find_adjecent(lines[i+1], number_indexes[i+1], symind))
#     elif i == len(lines) - 1:
#         r.append(find_adjecent(lines[i], number_indexes[i], symind))
#         r.append(find_adjecent(lines[i-1], number_indexes[i-1], symind))
#     else:
#         for j in range(0,3):
#             r.append(find_adjecent(lines[i-1+j], number_indexes[i-1+j], symind))

# print('ANSWER PART A: ', sum([sum(k) for k in r]))



def find_indexes_gears(input_string):
    numbers = re.finditer(r'\b\d+\b', input_string)
    ind_num = [(match.start() - 1, match.end()) for match in numbers]
    ind_sym = [index for index, char in enumerate(input_string) if char == "*"]
    
    return ind_sym, ind_num

def find_adjecent(num_range, sym_indexes):
    res = []

    for num in num_range:
        if any(num[0] <= sym <= num[1] for sym in sym_indexes):
            res.append(num)

    return res

lines = [line for line in open('input.txt').readlines()]

lines_indexes = [find_indexes_gears(line) for line in lines]
symbol_indexes, number_indexes = zip(*lines_indexes)


r = []
for i, symind in enumerate(symbol_indexes):
    # if i == 0:
    #     r.append(find_adjecent(lines[i], number_indexes[i], symind))
    #     r.append(find_adjecent(lines[i+1], number_indexes[i+1], symind))
    # elif i == len(lines) - 1:
    #     r.append(find_adjecent(lines[i], number_indexes[i], symind))
    #     r.append(find_adjecent(lines[i-1], number_indexes[i-1], symind))
    # else:
    #     for j in range(0,3):
    #         r.append(find_adjecent(lines[i-1+j], number_indexes[i-1+j], symind))

    if i == 0:
        r.append(((i,0),find_adjecent(number_indexes[i], symind)))
        r.append(((i,1),find_adjecent(number_indexes[i+1], symind)))
    elif i == len(lines) - 1:
        r.append(((i,-1),find_adjecent(number_indexes[i], symind)))
        r.append(((i,0),find_adjecent(number_indexes[i-1], symind)))
    else:
        for j in range(0,3):
            r.append(((i,j), find_adjecent(number_indexes[i-1+j], symind)))
for l in r:
    print(l)
# print('ANSWER PART B: ', sum([sum(k) for k in r]))
