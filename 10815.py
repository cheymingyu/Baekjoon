# 숫자 카드

N = int(input())
card_num = list(map(int, input().split()))
#print(card_num)
M = int(input())
check_num = list(map(int, input().split()))

card_num.sort()
#print(card_num)

def binary_search(num):
    start = 0
    end = len(card_num)-1

    while start <= end:
        mid = (start + end) // 2

        if card_num[mid] == num:
            return 1
        elif card_num[mid] < num:
            start = mid+1
        else:
            end = mid-1
    
    return 0



for i in range(M):
    a = check_num[i]
    print(binary_search(a), end=' ')
