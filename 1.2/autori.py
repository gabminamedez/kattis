phrase = input()

letters = phrase[0]
for i in range(1, len(phrase)):
    if phrase[i] == "-":
        letters += phrase[i + 1]

print(letters)
