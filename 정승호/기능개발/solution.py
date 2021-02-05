def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    done = 0
    while N != done:
        deploy = 0
        for index in range(done, N):
            progresses[index] += speeds[index]
        
        if progresses[done] >= 100:
            for i in range(done,N):
                if progresses[i] >= 100:
                    deploy += 1
                else:
                    break
            answer.append(deploy)
            done += deploy
            
    return answer
