# 연산자 끼워넣기

import sys

N = int(input())
A = list(map(int, input().split()))
O = list(map(int, input().split()))

max_cal = -sys.maxsize-1
min_cal = sys.maxsize

def recursion(num, idx, plus, minus, mul, div):
    global max_cal, min_cal
    if idx == N:
        max_cal = max(num, max_cal)
        min_cal = min(num, min_cal)
    
    if plus:
        recursion(num + A[idx], idx+1, plus-1, minus, mul, div)
    if minus:
        recursion(num - A[idx], idx+1, plus, minus-1, mul, div)
    if mul:
        recursion(num * A[idx], idx+1, plus, minus, mul-1, div)
    if div:
        recursion(int(num / A[idx]), idx+1, plus, minus, mul, div-1)
        
recursion(A[0], 1, O[0], O[1], O[2], O[3])

print(max_cal)
print(min_cal)