class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        n = len(nums)
        for i in range(n):
            map[nums[i]] = i
        
        for i in range(n):
            complement = target-nums[i]
            if complement in map and i!=map[complement]:
                return [i,map[complement]]
        return []
