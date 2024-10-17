class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []

        def backtrack(tmp):
            if len(nums) == len(tmp):
                answer.append(tmp[:])
                return

            for i in range(len(nums)):
                if nums[i] not in tmp:
                    tmp.append(nums[i])
                    backtrack(tmp)
                    tmp.pop()    

        backtrack([])
        return answer


