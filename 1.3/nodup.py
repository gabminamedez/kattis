import collections

string = input()
string = [word for word in string.split()]

counter = collections.Counter(string)

noDup = True
for i in counter.values():
    if i > 1:
        noDup = False
        break

if noDup:
    print("yes")
else:
    print("no")