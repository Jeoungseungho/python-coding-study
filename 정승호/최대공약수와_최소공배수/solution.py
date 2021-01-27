def gcb(a,b):
    i = min(a,b)
    while True:
        if a%i == 0 and b%i == 0:
            return i
        i-=1


def solution(n, m):
    return [gcb(n,m), n*m//gcb(n,m)]
