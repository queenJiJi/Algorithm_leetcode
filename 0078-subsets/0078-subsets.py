class Solution(object):
    def subsets(self, nums):
        ans = []
        def backtrack(start,result):
            result.append(ans[:])

            for i in range(start,len(nums)):
                ans.append(nums[i])
                backtrack(i+1,result)
                ans.pop()
            return result
        return backtrack(0,[])
        