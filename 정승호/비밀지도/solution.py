def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        or_bin = bin(arr1[i] | arr2[i])[2:]
        key = '0'*(n-len(or_bin)) + or_bin
        answer.append(key.replace('1', '#').replace('0', ' '))
    
    return answer
