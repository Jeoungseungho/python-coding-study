# bipartite 그래프 : 다른 그룹의 정점이 간선으로 연결되어져 있는(<=> 같은 그룹에 속한 정점끼리는 서로 인접하지 않도록 하는) 그래프
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0] * len(graph)

        for v in range(len(graph)):
            if not visited[v]:
                #               아래부턴 BFS 코드
                dq = deque([v])
                visited[v] = 1

                while dq:
                    idx = dq.popleft()

                    for i in graph[idx]:
                        if visited[i] == 0:
                            visited[i] = visited[idx] * -1
                            dq.append(i)
                        elif visited[i] == visited[idx]:
                            return False
        return True