class Solution(object):
    import heapq
    from collections import defaultdict
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((w,v))
            # graph[w].append((w,u))

        # costs = [-1]*(n+1)
        # costs[k] = 0
        costs ={}
        pq = []
        heapq.heappush(pq,(0,k))

        while pq:
            cur_cost, cur_v = heapq.heappop(pq)

            if cur_v not in costs:
                costs[cur_v] = cur_cost
            
                for cost, next_v in graph[cur_v]:
                    next_cost = cost+cur_cost
                    # if next_cost < costs[next_v]:
                    #     costs[next_v] = next_cost
                    heapq.heappush(pq,(next_cost, next_v))

        for node in range(1,n+1):
            if node not in costs:
                return -1
        return max(costs.values())
        # return costs[n]

        
        