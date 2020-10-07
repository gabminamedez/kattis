jon = input()
doc = input()

jonA = 0
for letter in jon:
    if letter == "a":
        jonA += 1

docA = 0
for letter in doc:
    if letter == "a":
        docA += 1

if jonA >= docA:
    print("go")
else:
    print("no")