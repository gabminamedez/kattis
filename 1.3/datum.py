import datetime

nums = input()
nums = [int(num) for num in nums.split()]

day = datetime.date(2009, nums[1], nums[0]).weekday()

if day == 0:
    print("Monday")
elif day == 1:
    print("Tuesday")
elif day == 2:
    print("Wednesday")
elif day == 3:
    print("Thursday")
elif day == 4:
    print("Friday")
elif day == 5:
    print("Saturday")
else:
    print("Sunday")
