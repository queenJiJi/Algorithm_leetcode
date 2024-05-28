class Solution(object):
    def twoSum(self, nums, target):
        nums = [[idx,val] for idx,val in enumerate(nums)]
        nums.sort(key=lambda x:x[1])
        l,r = 0,len(nums)-1

        while l<r:
            two_sum = nums[l][1]+nums[r][1]
            if two_sum>target:
                r-=1
            elif two_sum<target:
                l+=1
            else:
                return [nums[l][0], nums[r][0]]
        return False

        

            
                  