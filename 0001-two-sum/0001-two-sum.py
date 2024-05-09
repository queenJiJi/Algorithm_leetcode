class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # SOL1 - Brute Force
        # n = len(nums)
        # for i in range(n-1): 
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        # return []

        # SOL2 - Hashmap
        hashmap= {}
        n= len(nums)
        for i in range(n):
            hashmap[nums[i]] = i
        
        for i in range(n):
            complement = target - nums[i]
            if complement in hashmap and i!=hashmap[complement]:
                return [i, hashmap[complement]]
        return []
