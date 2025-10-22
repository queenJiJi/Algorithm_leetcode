class Solution(object):
    def subsets(self, nums):
        answer = []

        def backtrack(start, tmp):
            answer.append(tmp[:])

            if len(tmp) == len(nums):
                return

            for i in range(start,len(nums)):
                tmp.append(nums[i])
                backtrack(i+1,tmp)
                tmp.pop()
        backtrack(0,[])
        return answer
                