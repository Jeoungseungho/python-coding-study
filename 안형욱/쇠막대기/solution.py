# https://programmers.co.kr/learn/courses/30/lessons/42585

def solution(arrangement):
    answer = 0
    stick = 0
    # ()을 0으로 바꾸어 레이저로 인식
    arrangement = arrangement.replace('()', '0')

    while len(arrangement):
        target = arrangement.pop()
        if target == '0':
            answer += stick
        elif target == '(':
            stick += 1
        elif target == ')':
            answer += 1
            stick -= 1
    # for i in arrangement:
    #     if i=='0':
    #         answer+=stick
    #     elif i=='(':
    #         stick+=1
    #     elif i==')':
    #         answer+=1
    #         stick-=1
    return answer


# 밑에 solution은 테스트 케이스 통과하지 못하는 부분이 있는데 왜
# 그런지 모르겠네요... 같이 의논해보고 싶어서 남겨뒀습니다.
# def solution(arrangement):
#     answer = 0
#     stick = 0
#     laser = 0
#     arrangement = arrangement.replace('()', '0')
#     for i in arrangement:
#         if stick and i=='0':
#             laser+=1
#         elif i=='(':
#             stick+=1
#         elif i==')':
#             answer+=stick*laser+1
#             stick-=1
#             laser=0
#     return answer
