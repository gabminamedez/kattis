nums = []

for i in range(10):
    num = int(input())

    num = num % 42
    if num not in nums:
        nums.append(num)

print(len(nums))
