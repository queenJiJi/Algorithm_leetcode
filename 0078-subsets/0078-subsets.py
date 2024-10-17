class Solution(object):
    def subsets(self, nums):
        answer = []

        def backtrack(tmp):
            answer.append(tmp[:])

            if len(tmp) == len(nums):
                return

            for num in nums:
                if tmp and num <= max(tmp):
                    continue
                tmp.append(num)
                backtrack(tmp)
                tmp.pop()

        backtrack([])
        return answer