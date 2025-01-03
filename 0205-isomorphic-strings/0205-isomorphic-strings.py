class Solution(object):
    def isIsomorphic(self, s, t):
        s_list = []
        t_list = []

        for idx in s:
            s_list.append(s.index(idx))
        
        for idx in t:
            t_list.append(t.index(idx))

        return s_list == t_list
        