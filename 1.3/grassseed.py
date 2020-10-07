cost = float(input())
count = int(input())

total = 0
for i in range(count):
    nums = input()
    nums = [float(num) for num in nums.split()]

    total += nums[0] * nums[1]

print(total * cost)
