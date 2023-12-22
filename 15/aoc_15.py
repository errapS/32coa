
class Lens:
    def __init__(self, label, focal):
        self.label = label
        self.focal = focal


class BoxList(list):
    def __getitem__(self, label):
        if isinstance(label, str):
            for item in self:
                if item.label == label:
                    return item
            raise IndexError('no object labeled {!r}'.format(label))
        return list.__getitem__(self, label)

    def  remove_by_label(self, label):
        for i, item in enumerate(self):
            if item.label == label:
                del self[i]
                return item
        raise IndexError('no object labeled {!r}'.format(label))


def hash_value(c: str, cv: int):
    return ((cv + ord(c)) * 17) % 256


init_seq = open('15/input.txt').read().split(',')

res1 = 0
res2 = 0
boxes = {}

for step in init_seq:
    current_value_part1 = 0
    current_value_part2 = 0

    label = ''
    remove = False

    for char in step:
        current_value_part1 = hash_value(char, current_value_part1)

        if char.isalpha():
            current_value_part2 = hash_value(char, current_value_part2)
            label += char
        elif char.isdigit():
            focal = char
        elif char == '-':
            remove = True
    
    if remove:
        try:
            boxes[current_value_part2].remove_by_label(label)
        except:
            pass
    else:
        if current_value_part2 not in boxes:
            boxes[current_value_part2] = BoxList()

        try:
            if boxes[current_value_part2][label]:
                boxes[current_value_part2][label].focal = focal
            else:
                boxes[current_value_part2][label] = Lens(label, focal)

        except:
            boxes[current_value_part2].append(Lens(label, focal))


    res1 += current_value_part1


for k, v in boxes.items():
    res2 += sum([((k+1) * (i+1)*int(l.focal)) for i, l in enumerate(v)])


print('ANSWER PART A: ', res1)
print('ANSWER PART B: ', res2)

