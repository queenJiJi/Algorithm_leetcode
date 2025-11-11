class Solution(object):
    from collections import deque
    def findOrder(self, numCourses, prerequisites):
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        q = deque()
        visited = []

        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)
        
        while q:
            cur_v = q.popleft()
            visited.append(cur_v)

            for next_v in graph[cur_v]:
                indegree[next_v] -= 1
                if indegree[next_v] == 0:
                    q.append(next_v)
        return [] if numCourses!=len(visited) else visited
        