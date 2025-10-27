class Solution(object):
    def permute(self, nums):
        answer= []

        def backtrack(tmp):
            if len(tmp) == len(nums):
                answer.append(tmp[:])
                return

            for num in nums:
                if num not in tmp:
                    tmp.append(num)
                    backtrack(tmp)
                    tmp.pop()
        backtrack([])
        return answer
        