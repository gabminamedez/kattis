count = int(input())

for i in range(count):
    nums = input()
    nums = [int(num) for num in nums.split()]

    if nums[0] + nums[2] == nums[1]:
        print("does not matter")

    elif nums[0] + nums[2] <nums[1]:
        print("advertise")

    else:
        print("do not advertise")
