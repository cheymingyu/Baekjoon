import sys

string = sys.stdin.readline().rstrip()
string = string.upper()

check = []
dic = {}

while string:
    if string[0] in dic:
        dic[string[0]] += 1
    else:
        dic[string[0]] = 1
    string = string[1:]

print(dic)
max = max(dic.values())

for key in dic.keys():
    if dic[key] == max:
        check.append(key)

if len(check) >= 2:
    print("?")
else:
    print(check[0])

