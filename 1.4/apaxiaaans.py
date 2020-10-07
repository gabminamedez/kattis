word = input()

final = ""
prev = ""
for i in word:
    if i != prev:
        final += i
        prev = i

    else:
        prev = i
        continue

print(final)
