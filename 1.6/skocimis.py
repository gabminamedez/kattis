nums = input()
nums = [int(num) for num in nums.split()]

if (nums[1] - nums[0]) >= (nums[2] - nums[1]):
    print(nums[1] - nums[0] - 1)
else:
    print(nums[2] - nums[1] - 1)