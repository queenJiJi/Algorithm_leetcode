from bisect import bisect_left
class Solution(object):
    def search(self, nums, target):
        ans = bisect_left(nums,target)
        if ans!=len(nums) and target == nums[ans]:
            return ans
        return -1