class Solution(object):
    def twoSum(self, nums, target):
        nums = [(val,i) for i,val in enumerate(nums)] 
        nums.sort()
        l,r = 0, len(nums)-1
        while l<r:
            if nums[l][0]+nums[r][0] == target:
                return [nums[l][1],nums[r][1]]
            elif nums[l][0]+nums[r][0] < target:
                l+=1
            else:
                r-=1
        return -1
          

            
                  