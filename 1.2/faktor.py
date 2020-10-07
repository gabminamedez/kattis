import math

nums = input()
nums = [int(num) for num in nums.split()]

result = 0
infinite = 1
while infinite == 1:
    if math.ceil(result / nums[0]) == nums[1]:
        print(result)
        break

    result += 1
