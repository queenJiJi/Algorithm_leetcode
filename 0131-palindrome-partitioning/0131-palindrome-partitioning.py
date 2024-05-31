class Solution(object):
    def partition(self, s):
        n = len(s)
        ans,result = [], []  
        answer = []
        def backtrack(start):
            # base case
            if start == n:
                result.append(ans[:])

            for i in range(start,n):
                ans.append(s[start:i+1])
                backtrack(i+1)
                ans.pop()
            return result
        
        def isPalindrome(sub):
            return sub == sub[::-1]
        
        ret = backtrack(0)

        if ret: # check if palindrome
            for ch in ret:
                if all(isPalindrome(c) for c in ch):
                    answer.append(ch)
        return answer
