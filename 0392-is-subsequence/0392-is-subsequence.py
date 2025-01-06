class Solution(object):
    def isSubsequence(self, s, t):
        l,r = 0,0
        if len(s) == 0 :
            return True
        elif len(t) == 0:
            return False

        while l <len(s) and r<len(t):
            if s[l] == t[r]:
                if l == len(s)-1:
                    return True
                l+=1
                r+=1
            else:
                if r == len(t)-1:
                    return False
                else:
                    r+=1
        return False
        