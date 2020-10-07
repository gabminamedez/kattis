count = int(input())
nums = input()
nums = [int(num) for num in nums.split()]

total = 0
for i in range(count):
    if nums[i] < 0:
        total += 1

print(total)
