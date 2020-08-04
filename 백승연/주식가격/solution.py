prices = list(map(str, input().split(',')))
prices = list(map(int, prices))


def solution(prices):
    answer = []

    for i in range(len(prices)):
        cnt = 0
        stack = prices[i + 1:]
        while stack and stack[-1] >= prices[i]:
            cnt += 1
            stack.pop()
        answer.append(cnt)
    return answer


print(solution(prices))
