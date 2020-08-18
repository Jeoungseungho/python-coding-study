def Hanoi(n):
    if n==1:
        return 1
    return 2*Hanoi(n-1)+1

def printOrder(disk, start, mid, end):
    if disk == 1:
        print(start, end)
    else:
        printOrder(disk-1, start, end, mid)
        print(start, end)
        printOrder(disk-1, mid, start, end)

n = int(input())
disk = n
print(Hanoi(n))
printOrder(disk, 1, 2, 3)