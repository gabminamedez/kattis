nums = input()
nums = [int(num) for num in nums.split()]

otherH = nums[0] - nums[1]
otherV = nums[0] - nums[2]

h = max(nums[1], otherH)
v = max(nums[2], otherV)

print(v * h * 4)
