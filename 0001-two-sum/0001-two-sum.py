class Solution(object):
    def twoSum(self, nums, target):
        nums = [[idx,val] for idx,val in enumerate(nums)]
        nums.sort(key=lambda x: x[1])
        
        l,r=0,len(nums)-1

        while l<r:
            mean =nums[l][1]+nums[r][1]

            if target<mean:
                r-=1
            elif target>mean:
                l+=1
            else:
                return [nums[l][0],nums[r][0]]
        return False            