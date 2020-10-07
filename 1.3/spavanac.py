nums = input()
nums = [int(num) for num in nums.split()]

hour = nums[0]
minute = nums[1]

if 45 <= minute <= 59:
    minute -= 45
elif minute == 0:
    minute = 15
    hour -= 1
elif minute < 45:
    minute -= 45
    minute += 60
    hour -= 1

if hour < 0:
    hour += 24

print(str(hour) + " " + str(minute))
