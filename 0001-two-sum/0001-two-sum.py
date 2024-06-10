class Solution(object):
    def twoSum(self, nums, target):
        hash = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in hash:
                return [hash[complement], i]
            hash[nums[i]] = i        

            
                  