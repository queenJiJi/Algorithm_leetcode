from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        visited = [0] * len(graph)
        q = deque()
        def bfs(start_v):
            if visited[start_v]:
                return True

            q.append(start_v)    
            visited[start_v] = -1
            while q:
                cur_v = q.popleft()
                
                for next_v in graph[cur_v]:
                    if visited[next_v] == visited[cur_v]:
                        return False
                    elif not visited[next_v]:
                        visited[next_v] = -1*visited[cur_v]
                        q.append(next_v)
            return True
        
        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True
                



        
        