from bisect import bisect_left
class Solution(object):
    def search(self, nums, target):
        ans = bisect_left(nums,target)

        if ans<len(nums) and nums[ans] == target:
            return ans
        return -1














        # ans = bisect_left(nums,target)
        # if ans!=len(nums) and target == nums[ans]:
        #     return ans
        # return -1

        # l,r = 0,len(nums)-1
        
        # while l<=r:
        #     mean = (l+r)//2
        #     if nums[mean] ==target:
        #         return mean
        #     elif nums[mean]> target:
        #         r = mean-1
        #     else:
        #         l = mean+1
        # return -1