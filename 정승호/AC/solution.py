import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))
    reverse_flag = False
    zero_len_flag = False

    if n == 0:
        arr = deque()

    for ch in p:
        if ch == 'R':
            reverse_flag = not reverse_flag
        elif ch == 'D':
            if len(arr) == 0:
                zero_len_flag = True
                print("error")
                break
            else:
                if reverse_flag: arr.pop()
                else: arr.popleft()

    if not zero_len_flag:
        if reverse_flag:
            arr.reverse()
            print("[" + ",".join(arr) + "]")
        else:
            print("[" + ",".join(arr) + "]")

