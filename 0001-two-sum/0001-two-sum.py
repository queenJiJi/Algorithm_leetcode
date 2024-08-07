class Solution(object):
    def twoSum(self, nums, target):
        new_nums = []
        for idx, val in enumerate(nums):
            new_nums.append((val,idx))
        new_nums.sort(key=lambda x: x[0])
        start,end = 0, len(nums)-1

        while start<=end:
            if new_nums[start][0]+new_nums[end][0] == target:
                return [new_nums[start][1],new_nums[end][1]]
            elif new_nums[start][0]+new_nums[end][0] > target:
                end-=1
            else:
                start+=1
        return -1   

            
                  