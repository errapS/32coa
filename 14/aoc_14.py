import numpy as np 


CYCLES = 1_000_000_000
CYCLE_DICT = {}
CYCLE_SEQ = []
CYCLE_START = 0

def tilt(dish, start):
    global CYCLE_SEQ, CYCLE_START

    dish_tuple = tuple(map(tuple, dish))
    if dish_tuple in CYCLE_DICT:
        new_load = total_load(dish)

        if not CYCLE_SEQ:
            CYCLE_SEQ.append(new_load)
            CYCLE_START = start

        elif len(CYCLE_SEQ) > 2 and new_load == CYCLE_SEQ[1] and CYCLE_SEQ[0] == CYCLE_SEQ[-1]:
            print('ANSWER PART B: ',CYCLE_SEQ[(4 * CYCLES - CYCLE_START) % (len(CYCLE_SEQ)-1)])
            quit()

        elif CYCLE_SEQ:
            CYCLE_SEQ.append(new_load)

        return CYCLE_DICT[dish_tuple]

    for c in range(dish.shape[1]):
        o_indices = np.where(dish[:, c] == 'O')[0]
        hash_indices = np.concatenate((np.where(dish[:, c] == '#')[0], [dish.shape[1]]))
        for i in range(len(hash_indices)):
            if i == 0:
                valid_o = o_indices[o_indices < hash_indices[i]]
                k = 0
                for j in range(len(valid_o)):
                    dish[:, c][i+k], dish[:, c][valid_o[j]] = dish[:, c][valid_o[j]], dish[:, c][i+k]
                    k += 1
            else:
                valid_o = o_indices[(o_indices < hash_indices[i]) & (o_indices > hash_indices[i-1])]
                for j in range(len(valid_o)):
                    dish[:, c][hash_indices[i-1]+j+1], dish[:, c][valid_o[j]] = dish[:, c][valid_o[j]], dish[:, c][hash_indices[i-1]+j+1]
    
    del CYCLE_SEQ[:]
    CYCLE_DICT[dish_tuple] = dish.copy()

    return dish


def cycle_tilt(dish, cycles):
    dish = tilt(dish, 0)
    for i in range(1, cycles * 4 - 1):
        dish = tilt(np.rot90(dish, k=-1), i)

    return total_load(np.rot90(dish, k=-1))


def total_load(dish):
    tl = 0
    for row, rocks in enumerate(dish[::-1]):
        tl += np.count_nonzero(rocks == 'O') * (row + 1)

    return tl


dish_input = np.array([list(line.strip()) for line in open('14/input.txt').read().split('\n')])

print('ANSWER PART A: ', total_load(tilt(dish_input, 0)))

cycle_tilt(dish_input, CYCLES)
