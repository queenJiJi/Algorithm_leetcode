import heapq
class Solution(object):
    def smallestRange(self, nums):
        n = len(nums)
        for i in range(n):
            nums[i] = [(val, i) for val in nums[i]]

        max_val = -float('inf')
        pq = []

        for i in range(n):
            heapq.heappush(pq,nums[i][0])
            max_val = max(max_val, nums[i][0][0])

        idx_list = [0] * n
        answer = [pq[0][0], max_val]

        while 1:
            min_val, idx = heapq.heappop(pq)
            idx_list[idx] += 1

            if idx_list[idx] == len(nums[idx]):
                break

            next_num = nums[idx][idx_list[idx]]
            heapq.heappush(pq,next_num)
            max_val = max(max_val,next_num[0])

            if max_val - pq[0][0] < answer[1]-answer[0]:
                answer = [pq[0][0],max_val]
        return answer 