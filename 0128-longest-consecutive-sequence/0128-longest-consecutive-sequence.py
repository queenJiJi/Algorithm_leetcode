class Solution(object):
    def longestConsecutive(self, nums):
        nums = sorted(set(nums))
        cnt=1
        answer = 0
        if not nums:
            return 0
            
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                cnt+=1
            else:
                answer = max(answer, cnt)
                cnt = 1
        answer = max(answer,cnt)
        return answer
            
        