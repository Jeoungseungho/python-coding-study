N = int(input())
T = int(input())

graph = [[0] * N for i in range(N)]
visited = [0 * N for i in range(N)]
virus = []



for i in range(T):
    r,c = map(int, input().split())
    graph[r-1][c-1] = 1
    graph[c-1][r-1] = 1

    
    
    
def dfs(V):
    virus.append(V)
    visited[V-1] = 1
    for i in range(N):
        if visited[i]==0 and graph[V-1][i] == 1:
            dfs(i+1)
            
            
dfs(1)

print(len(virus)-1)
