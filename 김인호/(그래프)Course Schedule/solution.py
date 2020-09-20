from collections import deque

# 위상정렬
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        v, e = numCourses, len(prerequisites)
        graph = [[] for i in range(v)]
        indegree = [0] * v

        for i in range(e):
            a, b = prerequisites[i]
            graph[b].append(a)
            indegree[a] += 1

        result = []
        dq = deque()

        for i in range(v):
            if indegree[i] == 0:
                dq.append(i)

        while dq:
            now = dq.popleft()
            result.append(now)

            for i in graph[now]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    dq.append(i)

        if len(result) == numCourses:
            return True
        else:
            return False