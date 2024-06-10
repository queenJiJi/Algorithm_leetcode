class Solution(object):
    def longestConsecutive(self, nums):
        hashset = set(nums)
        count, answer = 0,0
        for val in hashset:
            if val-1 not in hashset:
                count = 1
                next = val+1
                while next in hashset:
                    count += 1
                    next += 1 
                answer = max(count, answer)
        return answer
        