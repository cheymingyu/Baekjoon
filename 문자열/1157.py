string = input().upper()

cnt = {}
check = []

for s in set(string):
    cnt[s] = string.count(s)

max_v = max(cnt.values())

for key in cnt.keys():
    if cnt[key] == max_v:
        check.append(key)


if len(check) >= 2:
    print("?")
else:
    print(check[0])

