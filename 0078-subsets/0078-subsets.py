from itertools import combinations
class Solution(object):
    def subsets(self, nums):
        answer= []
        for i in range(len(nums)+1):
            answer.extend(list(combinations(nums, i)))
        return answer        