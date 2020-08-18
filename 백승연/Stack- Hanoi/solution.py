'''
1번 탑 n-1개 원판 -> mid로 옮김
1번 탑 마지막 원판 -> dest 로 옮김
2번 탑 n-1개 원판 -> dest로 옮김
'''


def hanoi(n, start, mid, dest):
    if n == 1:
        print(start, 'move to', dest)
        return
    hanoi(n - 1, start, dest, mid)
    hanoi(1, start, mid, dest)
    hanoi(n - 1, mid, start, dest)


hanoi(3, '1번', '2번', '3번')
