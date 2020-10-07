count = int(input())

for i in range(count):
    string = input()

    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for element in string:
        if element.isalpha():
            if element.lower() in alpha:
                alpha.remove(element)
                if len(alpha) == 0:
                    break

    if len(alpha) == 0:
        print("pangram")
    else:
        output = "missing "
        for letter in alpha:
            output += letter
        print(output)