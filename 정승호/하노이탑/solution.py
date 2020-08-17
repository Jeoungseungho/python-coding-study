def hanoi(n, origin, destination, buffer):
    if n == 0:
        return 
    # n-1개의 원판을 1번 막대에서 2번 막대로 이동    
    hanoi(n-1, origin, buffer, destination)
    print(origin, destination)
    # n-1개의 원판을 2번에서 3번 막대로 이동
    hanoi(n-1,buffer, destination, origin)
    
k = int(input())
print(2**k - 1)
hanoi(k,1,3,2)
