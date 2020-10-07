def reverse(num):
    rev = 0
    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10

    return rev


nums = input()
nums = [int(num) for num in nums.split()]

print(max(reverse(nums[0]), reverse(nums[1])))
