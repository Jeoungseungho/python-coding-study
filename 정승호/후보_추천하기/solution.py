
N = int(input())
total_reco = int(input())
reco_student = list(map(int, input().split()))
frame = {}
cnt = 0

for i in range(total_reco):
    if reco_student[i] in frame:
        frame[reco_student[i]][0] += 1
    else:
        if len(frame) < N:
            frame[reco_student[i]] = [1,i]
        else:
            del_list = sorted(frame.items(), key= lambda x : (x[1][0], x[1][1]))
            del_key = del_list[0][0]
            del(frame[del_key])
            frame[reco_student[i]] = [1,i]

ans_list = list(sorted(frame.keys()))
print(*ans_list)

