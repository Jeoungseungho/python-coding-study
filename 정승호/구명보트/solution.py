def solution(people, limit):
    answer = 0
    i = 0; j = len(people)-1
    people.sort()
    while i<=j:
        answer+=1
        if people[i] + people[j] <= limit:
            i+=1
        j-=1
        
    return answer
