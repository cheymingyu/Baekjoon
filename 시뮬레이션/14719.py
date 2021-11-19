# 빗물

H, W = map(int, input().split())

block = list(map(int, input().split()))

rain = 0

for i in range(1, len(block)-1):
    left_max = max(block[:i+1])
    right_max = max(block[i+1:])
    
    wall = min(left_max, right_max)
    if wall > block[i]:
        rain += wall - block[i]
        
print(rain)