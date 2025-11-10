class Solution(object):
    from collections import deque
    def findOrder(self, numCourses, prerequisites):
        indegree = [0] * numCourses
        visited = []
        q = deque()

        graph = [[] for _ in range(numCourses)]

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)
        
        while q:
            cur_node = q.popleft()
            visited.append(cur_node)

            for next_node in graph[cur_node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    q.append(next_node)
        return [] if len(visited)!=numCourses else visited
                
        