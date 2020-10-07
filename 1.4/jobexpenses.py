count = input()
nums = input()
nums = [int(num) for num in nums.split()]

expenses = 0
incomes = 0

for num in nums:
    if num < 0:
        expenses += num
    else:
        incomes += num

if incomes >= expenses:
    print(abs(expenses))
else:
    print(incomes)