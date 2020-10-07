string = input()

tablet = 0
compass = 0
gear = 0
score = 0

for letter in string:
    if letter == "T":
        tablet += 1
    elif letter == "C":
        compass += 1
    else:
        gear += 1

score += tablet ** 2
score += compass ** 2
score += gear ** 2

while tablet > 0 and compass > 0 and gear > 0:
    score += 7

    tablet -= 1
    compass -= 1
    gear -= 1

print(score)