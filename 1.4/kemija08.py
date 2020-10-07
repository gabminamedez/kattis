string = input()

newString = ""
wasVowel = False

for letter in string:
    if letter in ("a", "e", "i", "o", "u") and not wasVowel:
        newString += letter
        wasVowel = True
    elif letter in ("a", "e", "i", "o", "u") and wasVowel:
        wasVowel = False
    elif letter not in ("a", "e", "i", "o", "u") and not wasVowel:
        newString += letter

print(newString)