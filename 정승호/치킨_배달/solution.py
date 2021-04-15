def dfs(idx, selected_chicken):
    global answer

    if idx > len(chicken):
        return
    if selected_chicken == M:
        result = 0
        for house in houses:
            min_dist = 99999999
            for chicken_idx, value in enumerate(chicken):
                if not is_checked[chicken_idx]:
                    continue
                min_dist = min(min_dist, (abs(house[0]-value[0])+abs(house[1]-value[1])))
            result += min_dist
        answer = min(result, answer)
        return
    is_checked[idx] = True
    dfs(idx+1, selected_chicken+1)
    is_checked[idx] = False
    dfs(idx+1, selected_chicken)




N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
houses = []
chicken = []
answer = 99999999

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append([i+1, j+1])
        elif city[i][j] == 2:
            chicken.append([i+1, j+1])

is_checked = [False]*(len(chicken)+1)
dfs(0,0)
print(answer)



