class Solution(object):
    def permute(self, nums):
        def backtrack(cur):
            # base case
            if len(cur) == len(nums):
                ans.append(cur[:]) 
                return
            
            for num in nums:
                if num not in cur:
                    cur.append(num)
                    backtrack(cur)
                    cur.pop()
        ans = []
        backtrack([])
        return ans

            