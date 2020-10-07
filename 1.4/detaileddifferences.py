num = input()

for i in range(int(num)):
    str1 = input()
    str2 = input()

    print(str1)
    print(str2)

    str3 = ""
    for letter1, letter2 in zip(str1, str2):
        if letter1 == letter2:
            str3 += "."
        else:
            str3 += "*"

    print(str3)
    print()