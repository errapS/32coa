import numpy as np 


def tilt(dish):
    for c in range(dish.shape[1]):
        o_indices = np.where(dish[:,c] == 'O')[0]
        hash_indices = np.concatenate((np.where(dish[:,c] == '#')[0], [dish.shape[1]]))
        for i in range(len(hash_indices)):
            if  i == 0:  
                valid_o = o_indices[o_indices < hash_indices[i]]
                k = 0
                for j in range(len(valid_o)):
                    dish[:,c][i+k], dish[:,c][valid_o[j]] = dish[:,c][valid_o[j]], dish[:,c][i+k] 
                    k += 1
            else:
                valid_o = o_indices[(o_indices < hash_indices[i]) & (o_indices > hash_indices[i-1])]
                for j in range(len(valid_o)):
                    dish[:,c][hash_indices[i-1]+j+1], dish[:,c][valid_o[j]] = dish[:,c][valid_o[j]], dish[:,c][hash_indices[i-1]+j+1]
    return dish


def cycle_tilt(dish, cycles):
    dish = tilt(dish)
    for _ in range(cycles * 4 - 1):
        dish = tilt(np.rot90(dish, k=-1))

    return np.rot90(dish, k=-1)
    

dish_input = np.array([list(line.strip()) for line in open('14/input.txt').read().split('\n')])

res1 = 0
for row, rocks in enumerate(tilt(dish_input)[::-1]):
    res1 += np.count_nonzero(rocks == 'O') * (row + 1)

print('ANSWER PART A: ', res1) 

res2 = 0
for row, rocks in enumerate(cycle_tilt(dish_input, 10_00)[::-1]):
    res2 += np.count_nonzero(rocks == 'O') * (row + 1)

print('ANSWER PART B: ', res2)



