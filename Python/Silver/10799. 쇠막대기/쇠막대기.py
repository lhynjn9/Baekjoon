lst = input()
sol = cnt = 0

for i in range(len(lst)):
    if lst[i] == '(' : # 막대기 추가
        cnt += 1
    else: # ')'
        cnt -= 1
        if lst[i-1] == '(': # 레이저
            sol += cnt
        else: # 막대기 제거
            sol += 1

print(f'{sol}')