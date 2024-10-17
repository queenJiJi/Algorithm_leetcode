class Solution(object):
    def partition(self, s):
        ans,result = [],[]
        n = len(s)
        def backtrack(start):
            if start == n:
                result.append(ans[:])
            
            for i in range(start,n):
                substr = s[start:i+1]
                if substr == substr[::-1]: # check if palindrome
                    ans.append(substr)
                    backtrack(i+1)
                    ans.pop()
            return result
        return backtrack(0)
