def sumDigs(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

count = int(input())

for i in range(count):
    num = input()
    num = num[::-1]
    num = [int(dig) for dig in num]

    for j in range(len(num)):
        if j % 2 == 1:
            new = num[j] * 2
            if new > 9:
                new = sumDigs(new)
            num[j] = new

    sum = 0
    for k in num:
        sum += k

    if sum % 10 == 0:
        print("PASS")
    else:
        print("FAIL")