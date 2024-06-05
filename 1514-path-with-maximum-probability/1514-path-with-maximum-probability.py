import heapq, collections
class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        graph = collections.defaultdict(list)

        for i in range(len(edges)):
            edges[i].append(succProb[i])
        
        for a,b,w in edges:
            graph[a].append((w,b))
            graph[b].append((w,a))

        # print(graph)

  

        prob = [0.0]*n
        pq = [(-1.0,start_node)]
        prob[start_node] = 1.0
        while pq:
            cur_prob, cur_node = heapq.heappop(pq)
            # if prob[cur_node] > cur_prob:
            #     continue
            
            for probability, next_node in graph[cur_node]:
                next_probability = -probability*cur_prob
                if next_probability > prob[next_node]:
                    prob[next_node] = next_probability
                    heapq.heappush(pq,(-next_probability,next_node))
        # print(prob)
        return prob[end_node]
        