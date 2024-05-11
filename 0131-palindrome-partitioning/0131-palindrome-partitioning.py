class Solution(object):
    def partition(self, s):
        part= []
        result = []
        
        def backtrack(start):
            if len(s) == start:
                result.append(part[:])
                return

            for i in range(start, len(s)):
                if isPalindrome(s,start,i):
                    part.append(s[start:i+1])
                    backtrack(i+1)
                    part.pop()

        def isPalindrome(s,left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left,right = left+1, right-1
            return True
            
        backtrack(0)
        return result
