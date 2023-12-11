import math

pathstr, *node_map = open('08/input.txt').read().split('\n\n')

path = list(pathstr.replace('R', '1').replace('L', '0'))
nodes = {}
for node in node_map[0].split('\n'):
    nodes[node.split('=')[0].strip()] = tuple(map(str, node.split('=')[1].strip().replace('(', '').replace(')', '').split(', '))) #node.split('=')[1].strip() 

node = nodes['AAA']
steps = 0
while True:
    idx = int(path.pop(0))
    path.append(str(idx))
    steps += 1
    if node[idx] == 'ZZZ':
        break
    node = nodes[node[idx]]

print('ANSWER PART B: ', steps)

nodes_a = res = {key: val for key, val in nodes.items() if key.endswith('A')}
steps_per_node = []
for key in nodes_a:
    steps = 0
    temp_path = path
    node = nodes_a[key]
    while True:
        idx = int(temp_path.pop(0))
        temp_path.append(str(idx))
        steps += 1
        if node[idx].endswith('Z'):
            steps_per_node.append(steps)
            break
        node = nodes[node[idx]]

res = math.lcm(*steps_per_node)
print('ANSWER PART B: ', res)
