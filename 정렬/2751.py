# 수 정렬하기 2

import sys

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    less_arr, equal_arr, big_arr = [], [], []
    pivot = arr[len(arr)//2]
    for i in arr:
        if i < pivot:
            less_arr.append(i)
        elif i == pivot:
            equal_arr.append(i)
        else:
            big_arr.append(i)
    
    return quick_sort(less_arr) + equal_arr + quick_sort(big_arr)

N = int(input())
s = []
for _ in range(N):
    s.append(int(sys.stdin.readline().rstrip()))

for i in sorted(s):
    sys.stdout.write(str(i)+'\n')
