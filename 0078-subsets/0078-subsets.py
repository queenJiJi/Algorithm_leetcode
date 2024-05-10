class Solution(object):
    def subsets(self, nums):
        def backtrack(start,cur,result):
            result.append(cur[:])

            for i in range(start,len(nums)):
                cur.append(nums[i])
                backtrack(i+1, cur,result)
                cur.pop()
            return result

        return backtrack(0,[],[])

        