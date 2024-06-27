import heapq, collections
class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        graph = collections.defaultdict(list)

        for i in range(len(edges)):
            edges[i].append(succProb[i])
        
        for u,v,w in edges:
            graph[u].append([w,v])
            graph[v].append([w,u])

        
        pq = [(-1.0, start_node)]
        prob = [0.0]*(n)
        prob[start_node] = 1.0

        while pq:
            cur_prob, cur_v = heapq.heappop(pq)
            if cur_v == end_node:
                return prob[end_node]
            
            for proba, next_v in graph[cur_v]:
                next_proba = (-proba * cur_prob)

                if next_proba>prob[next_v]:
                    heapq.heappush(pq,(-next_proba, next_v))
                    prob[next_v] =next_proba

        return 0
        