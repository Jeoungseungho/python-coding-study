def solution(N, stages):
    remain_user = len(stages)
    answer = {}
    for stage in range(1,N+1):
        if remain_user != 0:
            count = stages.count(stage)
            answer[stage] = count/remain_user
            remain_user -= count
        else:
            answer[stage] = 0
    
    return sorted(answer, key = lambda x : answer[x], reverse = True)
