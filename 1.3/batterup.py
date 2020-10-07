count = int(input())
nums = input()
nums = [int(num) for num in nums.split()]

dividend = 0
divisor = 0
for i in range(count):
    if nums[i] >= 0:
        dividend += nums[i]
        divisor += 1

print(dividend / divisor)
