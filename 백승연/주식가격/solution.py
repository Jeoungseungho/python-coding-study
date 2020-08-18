prices = list(map(str, input().split(',')))
prices = list(map(int, prices))


# 시간초과
# def solution(prices):
#     answer = []
#
#     for i in range(len(prices)):
#         cnt = 0
#         stack = prices[i + 1:]
#         while stack and stack[-1] >= prices[i]:
#             cnt += 1
#             stack.pop()
#         answer.append(cnt)
#     return answer


#프로그래머스 풀이
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer


print(solution(prices))
