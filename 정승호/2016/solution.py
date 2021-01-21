def solution(a, b):
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31,29,31, 30, 31, 30,31, 31, 30, 31, 30, 31]
    total = 0
    
    for i in range(a-1):
        total += month[i]
    total += b-1
    
    answer = week[total%7]
    
    return answer
