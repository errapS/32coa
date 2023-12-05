import re

data = open('05/input.txt').readlines()
seeds = [int(v) for v in data[0][6:].split()]

keys = ["seeds_to_soil", "soil_to_fertilizer", "fertilizer_to_water", "water_to_light",
        "light_to_temperature", "temperature_to_humidity", "humidity_to_location"]

seed_maps = {seed: {key: seed for key in keys} for seed in seeds}

checked_seeds = []
map_index = -1
for line in (data):
    if line == '\n':
        for seed in seeds:
            if seed not in checked_seeds:
                seed_maps[seed][keys[map_index]] = seed_maps[seed][keys[map_index-1]]
                if map_index < 6:
                    seed_maps[seed][keys[map_index+1]] = seed_maps[seed][keys[map_index]]

        checked_seeds = []
        map_index += 1
        continue

    for seed in seeds:
        if re.match("^[0-9 ]+$", line):
            vals = [int(v) for v in line.split()]
            i = 0
            current_value = seed_maps[seed][keys[map_index]] 

            if  vals[1] <= current_value < vals[1] + vals[2] and seed not in checked_seeds:
                checked_seeds.append(seed)
                seed_maps[seed][keys[map_index]] = vals[0] + current_value - vals[1]
                if map_index < 6:
                    seed_maps[seed][keys[map_index+1]] = seed_maps[seed][keys[map_index]]
            
locations = []    
for seed, seed_map in seed_maps.items():
    locations.append(seed_map['humidity_to_location'])

print('ANSWER PART A: ', min(locations))


inp = open('05/input.txt').readlines()
data = [int(v) for v in inp[0].split(':')[1].split()]

seeds = []

for i in range(0, len(data), 2):
    seeds.append((data[i], data[i] + data[i + 1]))

maps_raw = ''.join(inp[1:]).split('\n\n')

maps = []
for m in maps_raw:
    t = []
    for line in m.splitlines():
        if re.match("^[0-9 ]+$", line):
            t.append(list(map(int, line.split())))
    maps.append(t)

for seed_map in maps:
    locations = []

    for start, end in seeds:
        for val, seed_idx, r in seed_map:
            overlap_start = max(start, seed_idx)
            overlap_end = min(end, seed_idx + r)

            if overlap_start < overlap_end:
                locations.append((overlap_start - seed_idx + val, overlap_end - seed_idx + val))
                if overlap_start > start:
                    seeds.append((start, overlap_start))
                if end > overlap_end:
                    seeds.append((overlap_end, end))
                break
        else:
            locations.append((start, end))

    seeds = locations

print('ANSWER PART B: ', min(seeds)[0])

