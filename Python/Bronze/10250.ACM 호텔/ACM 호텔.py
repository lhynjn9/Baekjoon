T = int(input())

for i in range(0, T):
    H, W, N = map(int, input().split())
    
    if N % H == 0:
        floor = H * 100
        num = N // H
    else:
        floor = (N % H) * 100
        num = (N // H) + 1

    print(floor + num)