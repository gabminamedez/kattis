nums = input()
nums = [int(num) for num in nums.split()]

if nums[0] == nums[1] and nums[0] != 0:
    print("Even " + str(nums[0] + nums[1]))

elif nums[0] != nums[1]:
    print("Odd " + str(max(nums[0], nums[1]) * 2))

else:
    print("Not a moose")
