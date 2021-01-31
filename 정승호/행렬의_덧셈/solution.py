def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[0])):
            total = arr1[i][j] + arr2[i][j]
            temp.append(total)
        answer.append(temp)
        
    return answer
