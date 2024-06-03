from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visited = []
        indegree= [0]*numCourses
        for v,u in prerequisites:
            graph[u].append(v)
            indegree[v]+=1
        
        q = deque()

        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)

        while q:
            cur_v = q.popleft()
            visited.append(cur_v)

            for next_v in graph[cur_v]:
                indegree[next_v] -=1

                if indegree[next_v] == 0:
                    q.append(next_v)
        return True if len(visited) == numCourses else False 
        

    
       