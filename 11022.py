# A+B

T = int(input())
add_list = [list(map(int, list(input().split()))) for _ in range(T)]

for i in add_list:
    print(i)

for i in range(T):
    A = add_list[i][0]
    B = add_list[i][1]
    sum = A+B
    print("Case #{0}: {1} + {2} = {3}".format(i+1, A, B, sum))