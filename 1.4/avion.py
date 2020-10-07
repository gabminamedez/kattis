strings = []

one = input()
strings.append(one)
two = input()
strings.append(two)
three = input()
strings.append(three)
four = input()
strings.append(four)
five = input()
strings.append(five)

nums = []
for i in range(len(strings)):
    if "FBI" in strings[i]:
        nums.append(i + 1)

final = ""
if len(nums) > 0:
    for i in range(len(nums)):
        final += str(nums[i]) + " "
    print(final)

else:
    print("HE GOT AWAY!")
