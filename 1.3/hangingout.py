nums = input()
nums = [int(num) for num in nums.split()]

notAllowed = 0
curr = 0

for i in range(nums[1]):
    event = input()

    event = [word for word in event.split()]
    if event[0] == "enter":
        curr += int(event[1])
        if curr > nums[0]:
            notAllowed += 1
            curr -= int(event[1])
    elif event[0] == "leave":
        curr -= int(event[1])

print(notAllowed)