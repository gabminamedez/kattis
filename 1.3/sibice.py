import math

nums = input()
nums = [int(num) for num in nums.split()]

diagonal = math.sqrt(nums[1]**2 + nums[2]**2)
for i in range(nums[0]):
    num = int(input())

    if num <= nums[1] or num <= nums[2] or num <= diagonal:
        print("DA")
    else:
        print("NE")
