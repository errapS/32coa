
inp = open('04/input.txt').readlines()
cards = [1 for _ in range(0,len(inp))]
res = 0
for idx, line in enumerate(inp):
    line = line.split(":")[1]
    win_nums, nums = line.split("|")
    win_nums, nums = win_nums.split(), nums.split()

    matches = set(win_nums) & set(nums)
    if len(matches) > 0:
        res += 2**(len(matches)-1)

    for i in range(len(matches)):
        cards[idx + 1 + i] += cards[idx]

print('ANSWER PART A: ', res)
print('ANSWER PART B: ', sum(cards))
    