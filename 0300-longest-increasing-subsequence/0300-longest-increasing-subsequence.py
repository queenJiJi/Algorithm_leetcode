class Solution(object):
    def lengthOfLIS(self, nums):
        dp= [1]* len(nums) # 아무리 길이가 짧아도 본인 길이1일테니까 dp테이블의 원소를 모두 1로 초기화

        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
        