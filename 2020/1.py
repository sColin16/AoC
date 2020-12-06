
pair_nums = set()

def get_pair_sum(nums, target):
    pair_nums = set()
    
    for num in nums:
        if num in pair_nums:
            return (num, target - num)
        else:
            pair_nums.add(target - num)

    return False

with open("1-input.txt", "r") as f:
    NUMS = [int(num) for num in f.readlines()]

x, y = get_pair_sum(NUMS, 2020)
print(x * y)

for i, num in enumerate(NUMS):
    pair = get_pair_sum(NUMS[i:], 2020 - num)

    if pair:
        print(num * pair[0] * pair[1])
        break

