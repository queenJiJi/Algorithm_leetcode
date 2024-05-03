import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)   
        for time in times:
            graph[time[0]].append((time[2],time[1]))
        
        pq =[]
        costs = {}
        heapq.heappush(pq, (0,k))

        while pq:
            cur_cost,cur_v = heapq.heappop(pq)
            if cur_v not in costs:
                costs[cur_v] = cur_cost
                for cost, next_v in graph[cur_v]:
                    next_cost = cur_cost + cost
                    heapq.heappush(pq,(next_cost, next_v))
        for i in range(1,n+1):
            if i not in costs:
                return -1

        return max(costs.values())