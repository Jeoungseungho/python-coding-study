def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.add(numbers[i] + numbers[j])
    answer = sorted(list(answer))
    return answer
