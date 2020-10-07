nums = input()
nums = [int(num) for num in nums.split()]

while nums[0] != 0 and nums[1] != 0:
    if nums[0] >= nums[1]:
        a = nums[0] / nums[1]
        b = nums[0] % nums[1]
        c = (nums[0] - int(b)) / int(a)
    elif nums[0] < nums[1]:
        a = 0
        b = nums[0]
        c = nums[1]

    print(str(int(a)) + " " + str(int(b)) + " / " + str(int(c)))

    nums = input()
    nums = [int(num) for num in nums.split()]