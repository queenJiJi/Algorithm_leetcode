from bisect import bisect_left
class Solution(object):
    def search(self, nums, target):
        answer = bisect_left(nums,target)
        if answer!=len(nums) and target == nums[answer]:
            return answer
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