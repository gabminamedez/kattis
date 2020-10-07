nums = input()
nums = [int(num) for num in nums.split()]

result = ""
result += str(1 - nums[0])
result += " " + str(1 - nums[1])
result += " " + str(2 - nums[2])
result += " " + str(2 - nums[3])
result += " " + str(2 - nums[4])
result += " " + str(8 - nums[5])

print(result)
