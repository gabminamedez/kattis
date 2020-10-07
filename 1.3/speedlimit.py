num = int(input())

while num != -1:
    prev = 0
    total = 0
    for i in range(num):
        nums = input()
        nums = [int(num) for num in nums.split()]

        total += nums[0] * (nums[1] - prev)
        prev = nums[1]

    print(str(total) + " miles")
    num = int(input())
