count = int(input())

days = set()
for i in range(count):
    nums = input()
    nums = [int(num) for num in nums.split()]

    for i in range(nums[0], nums[1] + 1):
        days.add(i)

print(len(days))