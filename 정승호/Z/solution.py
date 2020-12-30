n, r, c = map(int, input().split())
answer = 0

while n >= 1:
    temp = 2 ** (n - 1)
    if n == 1:
        if r is 0 and c is 1:
            answer += 1
        elif r is 1 and c is 0:
            answer += 2
        elif r is 1 and c is 1:
            answer += 3
        break

    if r < temp <= c:  # 2사분면
        answer += temp ** 2
        c -= temp
    elif c < temp <= r:  # 3사분면
        answer += (temp ** 2) * 2
        r -= temp
    elif temp <= c and temp <= r:  # 4 사분면
        answer += (temp ** 2) * 3
        r -= temp
        c -= temp

    n -= 1

print(answer)
