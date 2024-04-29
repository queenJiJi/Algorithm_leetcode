class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dict = {}
        answer =0

        for i in nums:
            nums_dict[i] = True

        for num in nums_dict:
            if num-1 not in nums_dict:
                count = 1
                target = num+1
                while target in nums_dict:
                    count +=1
                    target +=1
                answer = max(answer,count)
        return answer