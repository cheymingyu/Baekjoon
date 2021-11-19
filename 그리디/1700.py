# 멀티탭 스케줄링

N, K = map(int, input().split())
elec = list(map(int, input().split()))

power = [0 for _ in range(N)]
count = 0

for e in range(len(elec)):
    if elec[e] in power:
        continue
    elif 0 in power:
        for i in range(len(power)):
            if power[i] == 0:
                break;
        power[i] = elec[e]
    else:
        loc = [101 for _ in range(N)]
        for i in range(len(power)):
            if power[i] in elec[e+1:]:
                loc[i] = elec[e+1:].index(power[i])
        
        latest_loc = loc.index(max(loc))
        power[latest_loc] = elec[e]
        count += 1

print(count)
