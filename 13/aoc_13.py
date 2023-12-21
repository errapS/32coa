import numpy as np

def find_sequence(pat, ep):
    unique_rows, counts = np.unique(pat, axis=0, return_counts=True)
    duplicate_rows = unique_rows[counts > 1]
    ranges =  [np.where(np.all(pat == row, axis=1))[0]+1 for row in duplicate_rows]
    pairs = [(arr[i], arr[j]) for arr in ranges for i in range(len(arr)) for j in range(i+1, len(arr))]

    seq = [(0,0)]
    perfect = 0
    for pair in pairs:
        temp_seq = [pair]
        i = 1
        while pair[0] - i >= 1 and pair[1] + i <= ep :
            temp_seq.append((pair[0] - i, pair[1] + i))
            i += 1
        
        if all(p in pairs for p in temp_seq) and temp_seq[0][1] - temp_seq[0][0] == 1:
            if all(x1[0] - x2[0] == 1 and x2[1] - x1[1] == 1 for x1, x2 in zip(temp_seq[:-1], temp_seq[1:])):
                if temp_seq[0][0] > seq[0][0]: 
                    seq = temp_seq
                    if temp_seq[-1][0] == 1 or temp_seq[-1][1] == ep:
                        perfect = 1
            
    if seq[0] == (0,0):
        if pairs and pairs[0][1] - pairs[0][0] == 1:
            return pairs[0][0], perfect
        else:
            return 0, perfect
        
    return seq[0][0], perfect


def find_sequence_part2(pat, ep):
    unique_rows, counts = np.unique(pat, axis=0, return_counts=True)
    duplicate_rows = unique_rows[counts > 1]
    ranges =  [np.where(np.all(pat == row, axis=1))[0]+1 for row in duplicate_rows]
    pairs = [(arr[i], arr[j]) for arr in ranges for i in range(len(arr)) for j in range(i+1, len(arr))]
    seq = [(0,0)]

    if sum(1 for a, b in zip(pat[0], pat[1]) if a != b) == 1:
        return 1, 1, True
    elif sum(1 for a, b in zip(pat[ep-2], pat[-1]) if a != b) == 1:
        return ep-1, 1, True
    
    perfect = 0
    inv_flag = False
    for pair in pairs:
        temp_seq = [pair]
        temp_pairs = [*pairs]
        
        i = 1
        if pair[1] - pair[0] != 0:
            while pair[0] + i < pair[1] - i:
                temp_seq = [(pair[0] + i, pair[1] - i)]
                i += 1
        i = 1
        tp = temp_seq[0]
        while tp[0] - i >= 1 and tp[1] + i <= ep :
            temp_seq.append((tp[0] - i, tp[1] + i))
            i += 1
           
        invalid_pairs = [i for i, p in enumerate(temp_seq) if p not in pairs]
        if len(invalid_pairs) == 1 and sum(1 for a, b in zip(pat[temp_seq[invalid_pairs[0]][0]-1], pat[temp_seq[invalid_pairs[0]][1]-1]) if a != b) == 1:
            temp_pairs.append(temp_seq[invalid_pairs[0]])
        if all(p in temp_pairs for p in temp_seq) and temp_seq[0][1] - temp_seq[0][0] == 1:
            if all(x1[0] - x2[0] == 1 and x2[1] - x1[1] == 1 for x1, x2 in zip(temp_seq[:-1], temp_seq[1:])):
                if not inv_flag and invalid_pairs: 
                    inv_flag = True 
                    seq = temp_seq
                    if temp_seq[-1][0] == 1 or temp_seq[-1][1] == ep:
                        perfect = 1
                elif inv_flag and temp_seq[0][0] > seq[0][0] and invalid_pairs:
                    seq = temp_seq
                    if temp_seq[-1][0] == 1 or temp_seq[-1][1] == ep:
                        perfect = 1
                elif not inv_flag and temp_seq[0][0] > seq[0][0]: 
                    seq = temp_seq
                    if temp_seq[-1][0] == 1 or temp_seq[-1][1] == ep:
                        perfect = 1

    if seq[0] == (0,0):
        if pairs and pairs[0][1] - pairs[0][0] == 1:
            return pairs[0][0], perfect, inv_flag
        else:
            return 0, perfect, inv_flag
        
    return seq[0][0], perfect, inv_flag


patterns = open('13/input.txt').read().split('\n\n')

res1 = 0
res2 = 0
for i, pattern in enumerate(patterns):
    pr = np.array([list(line.strip()) for line in pattern.split('\n')])

    rot = [''.join(row[j] for row in pattern.split('\n')[::-1]) for j in range(len(pattern.split('\n')[0]))]
    pattern = '\n'.join(rot)
    pc = np.array([list(line.strip()) for line in pattern.split('\n')])

    mr, perf_row = find_sequence(pr, len(pc[0]))
    mc, perf_col = find_sequence(pc,  len(pr[0]))

    if perf_col > perf_row:
        res1 += mc
    else:
        res1 += mr * 100

    mr2, perf_row2, smudge_row = find_sequence_part2(pr, len(pc[0]))
    mc2, perf_col2, smudge_col = find_sequence_part2(pc,  len(pr[0]))

    if smudge_col:
        res2 += mc2
    elif smudge_row:
        res2 += mr2 * 100
    elif mc2 > mr2:
        res2 += mc2
    else:
        res2 += mr2 * 100
      
print('ANSWER PART A: ', res1)
print('ANSWER PART B: ', res2)
