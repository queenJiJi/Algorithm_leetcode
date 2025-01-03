from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        r_dic = Counter(ransomNote)
        m_dic = Counter(magazine)
           
        for char, cnt in r_dic.items():
            if m_dic[char] < cnt:
                return False
        return True

