class Solution(object):
    def wordPattern(self, pattern, s):
        def converting(pair):
            dic = {}
            result = []
            for idx,val in enumerate(pair):
                if val not in dic:
                    dic[val] = idx
                result.append(dic[val])

            return result
        
        words = s.split()
        return converting(pattern) == converting(words)