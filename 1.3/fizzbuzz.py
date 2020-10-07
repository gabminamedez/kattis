nums = input()
nums = [int(num) for num in nums.split()]

for i in range(1, nums[2] + 1):
    if i % nums[0] == 0 and i % nums[1] == 0:
        print("FizzBuzz")

    elif i % nums[0] == 0:
        print("Fizz")

    elif i % nums[1] == 0:
        print("Buzz")

    else:
        print(i)
