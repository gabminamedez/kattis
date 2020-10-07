count = int(input())

for i in range(count):
    nums = input()
    nums = [int(num) for num in nums.split()]

    s1 = 0
    s2 = 0
    s3 = 0

    for j in range(1, nums[1] + 1):
        s1 += j

    counterA = 0
    counterB = 0
    iter = 1
    while counterA != nums[1] or counterB != nums[1]:
        if iter % 2 == 1:
            s2 += iter
            counterA += 1
        else:
            s3 += iter
            counterB += 1
        iter += 1

    print(str(nums[0]) + " " + str(s1) + " " + str(s2) + " " + str(s3))