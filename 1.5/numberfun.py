counter = int(input())

for i in range(counter):
    nums = input()
    nums = [int(num) for num in nums.split()]

    if nums[0] + nums[1] == nums[2]:
        print("Possible")
    elif nums[1] + nums[0] == nums[2]:
        print("Possible")
    elif nums[0] - nums[1] == nums[2]:
        print("Possible")
    elif nums[1] - nums[0] == nums[2]:
        print("Possible")
    elif nums[0] * nums[1] == nums[2]:
        print("Possible")
    elif nums[1] * nums[0] == nums[2]:
        print("Possible")
    elif nums[0] / nums[1] == nums[2]:
        print("Possible")
    elif nums[1] / nums[0] == nums[2]:
        print("Possible")
    else:
        print("Impossible")
