nums = input()
nums = [int(num) for num in nums.split()]
letters = input()

nums.sort()

new = []
for letter in letters:
    if letter == "A":
        new.append(nums[0])
    elif letter == "B":
        new.append(nums[1])
    elif letter == "C":
        new.append(nums[2])

print(str(new[0]) + " " + str(new[1]) + " " + str(new[2]))