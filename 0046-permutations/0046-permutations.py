class Solution(object):
    def permute(self, nums):
        # def backtrack(cur):
        #     # base case
        #     if len(cur) == len(nums):
        #         ans.append(cur[:]) 
        #         return
            
        #     for num in nums:
        #         if num not in cur:
        #             cur.append(num)
        #             backtrack(cur)
        #             cur.pop()
        # ans = []
        # backtrack([])
        # return ans

        ans,result =[],[]
        n = len(nums)
        def backtrack():
            if n == len(ans):
                result.append(ans[:])
                return
            
            for i in range(n):
                if nums[i] not in ans:
                    ans.append(nums[i])
                    backtrack()
                    ans.pop()
            return result
        return backtrack()        