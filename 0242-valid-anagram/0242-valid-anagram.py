from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        s_dic = Counter(s)
        t_dic = Counter(t)

        if len(s) != len(t):
            return False

        for val, cnt in s_dic.items():
            if t_dic[val] < cnt:
                return False
        return True
        