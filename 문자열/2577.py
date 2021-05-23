A = int(input())
B = int(input())
C = int(input())

result = A*B*C
result = str(result)
tmp = []

for i in result:
    tmp.append(i)


answer = []
for i in range(10):
    answer.append(tmp.count(str(i)))

for i in answer:
    print(i)