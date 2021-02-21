def solution(a):
    answer = 2
    if 0 <= len(a) <= 2:
        return len(a)
    temp = set()
    left, right = a[0], a[-1]
    for i in range(1, len(a)-1):
        if left > a[i]:
            temp.add(a[i])
            left = a[i]
        if right > a[-1-i]:
            temp.add(a[-1-i])
            right = a[-1-i]
            
    return answer + len(temp)
