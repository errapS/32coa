reports = open('09/input.txt').read().split('\n')

def next_value(seq):
    diff = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
    if diff[-1] != 0:
        return diff[-1] + next_value(diff)
    return diff[-1]

def previous_value(seq):
    diff = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
    if diff[-1] != 0:
        return diff[0] - previous_value(diff)
    return diff[0]

res_a = 0
res_b = 0
for line in reports:
    seq = [int(val) for val in line.split(' ')]
    diff_a = next_value(seq)
    res_a += seq[-1] + diff_a
    
    diff_b = previous_value(seq)
    res_b += seq[0] - diff_b

print('ANSWER A: ', res_a)
print('ANSWER B: ', res_b)

