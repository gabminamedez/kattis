gunnar = input()
emma = input()

gunnar = [int(num) for num in gunnar.split()]
emma = [int(num) for num in emma.split()]

gunnarSum = 0
for num in gunnar:
    gunnarSum += num

emmaSum = 0
for num in emma:
    emmaSum += num

if gunnarSum == emmaSum:
    print("Tie")
elif gunnarSum > emmaSum:
    print("Gunnar")
else:
    print("Emma")