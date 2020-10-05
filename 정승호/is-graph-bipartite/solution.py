class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        
        def dfs(graph, node, colors, color):
            colors[node] = color
            for node_to in graph[node]:
                if node_to in colors:
                    if colors[node_to] == colors[node]:
                        return False
                else :
                    if not dfs(graph, node_to, colors, color*-1):
                        return False
            return True
        
        for node_from in range(len(graph)):
            if node_from not in colors and not dfs(graph, node_from, colors, 1):
                return False
        return True
