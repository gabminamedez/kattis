count = int(input())

for i in range(count):
    string = input()
    string = [str(word) for word in string.split()]

    if string[0] == "Simon" and string[1] == "says":
        printOut = ""
        for j in range(2, len(string)):
            printOut += string[j] + " "

        printOut.rstrip()
        print(printOut)