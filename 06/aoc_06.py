import re

times, distances = open('06/input.txt').read().split('\n')
times = [int(t.strip()) for t in re.findall(r'(\s\d+)', times)]
distances = [int(d.strip()) for d in re.findall(r'(\s\d+)', distances)]

races = zip(times,distances)
speed_options = 1

for time, dist in races:
    for i in range(1,time):
        time_diff = time - i
        if time_diff * i > dist:
            speed_options *= time_diff + 1 - i
            break

print('ANSWER PART A: ', speed_options)

time2 = int(''.join(str(x) for x in times))
distance2 = int(''.join(str(x) for x in distances))

speed_options2 = 1

for i in range(1,time2):
    time_diff = time2 - i
    if time_diff * i > distance2:
        speed_options2 *= time_diff + 1 - i
        break
    
print('ANSWER PART B: ', speed_options2)
