string = input()

whitespace = 0
lowercase = 0
uppercase = 0
symbols = 0
for i in range(len(string)):
    if ord(string[i]) == 95:
        whitespace += 1

    elif ord(string[i]) >= 97 and ord(string[i]) <= 122:
        lowercase += 1

    elif ord(string[i]) >= 65 and ord(string[i]) <= 90:
        uppercase += 1

    else:
        symbols += 1

print(whitespace / len(string))
print(lowercase / len(string))
print(uppercase / len(string))
print(symbols / len(string))
