class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l+=1
            else:
                r-=1
                
        return -1