import collections, heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        # 인접리스트로 변환
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[2],time[1]))

        # 다익스트라 알고리즘 적용
        pq = [(0,k)]
        costs = {} # 비용을 업데이트 해주며 일종의 방문표시
        
        while pq:
            cur_cost,cur_v = heapq.heappop(pq)

            if cur_v not in costs:
                costs[cur_v] = cur_cost

                for cost,next_v in graph[cur_v]:
                    next_cost = cur_cost + cost
                    heapq.heappush(pq,(next_cost,next_v))
        
        # 전체노드를 방문했나 확인
        for node in range(1,n+1):
            if node not in costs:
                return -1
        return max(costs.values())
