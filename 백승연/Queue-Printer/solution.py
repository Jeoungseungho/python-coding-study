from collections import deque


def solution(priorities, location):
    answer = 0

    Q = [(pos, val) for pos, val in enumerate(deque(priorities))]
    Q = deque(Q)

    while Q:
        cur = Q.popleft()
        if any(cur[1] < x[1] for x in Q):
            Q.append(cur)
            continue
        answer += 1
        if cur[0] == location:
            break

    return answer