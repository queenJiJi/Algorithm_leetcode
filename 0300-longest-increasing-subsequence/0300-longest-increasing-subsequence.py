from bisect import bisect_left
class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n
        for i in range(1,n):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
        # SOL 1- DP
        # dp= [1]* len(nums) # 아무리 길이가 짧아도 본인 길이1일테니까 dp테이블의 원소를 모두 1로 초기화

        # for i in range(1,len(nums)):
        #     for j in range(0,i):
        #         if nums[i]>nums[j]:
        #             dp[i] = max(dp[i], dp[j]+1)
        # return max(dp)
        
        # SOL 2- binary seacrh

        # ans = []
        # for num in nums:
        #     index = bisect_left(ans,num)

        #     if index == len(ans):
        #         ans.append(num)
        #     else:
        #         ans[index] = num
        # return len(ans)