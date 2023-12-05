import re

with open('01/input.txt') as f:
    input = f.readlines()

numbers1 = [re.sub(r'\D', '', line) for line in input]

print('ANSWER PART 1: ', sum([int(num[0]+num[-1]) if len(num) > 1 else int(num + num) for num in numbers1]))

with open('01/input2.txt') as f:
    input2 = f.readlines()

def replaceStrings(line: str):
    str_nums = {'sevenineightwone': '79821', 'sevenineightwo': '7982', 'sevenineighthree': '7983', 'nineightwone': '9821', 'fiveightwone': '5821', 'threeightwone': '3821',
                'twoneighthree': '2183', 'nineightwo': '982', 'nineighthree': '983', 'nineighthree': '983', 'eightwone': '821', 'sevenineight': '798', 'fiveightwo': '582',
                'fiveighthree': '583', 'threeightwo': '382', 'twoneight': '218', 'oneightwo': '182', 'nineight': '98', 'eightwo': '82', 'eighthree': '83', 'sevenine': '79',
                'fiveight': '58', 'threeight': '38', 'twone': '21', 'oneight': '18', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                'eight': '8', 'nine': '9'}

    str_nums = dict((re.escape(k), v) for k, v in str_nums.items())
    pattern = re.compile("|".join(str_nums.keys()))
    line = pattern.sub(lambda m: str_nums[re.escape(m.group(0))], line)
    return line

numbers2 = [re.sub(r'\D', '', replaceStrings(line)) for line in input2]
print('ANSWER PART 2: ', sum([int(num[0]+num[-1]) if len(num) > 1 else int(num + num) for num in numbers2]))


