'''
https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
'''

def solution(prices):
    length = len(prices)

    result = [0]*length
    for i in range(length):
        sum = 0
        for j in range(i+1,length):
            sum += 1
            if prices[i] > prices[j]:
                break
        result[i] = sum
    return result