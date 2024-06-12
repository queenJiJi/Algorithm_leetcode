import collections
class Solution(object):
    def groupAnagrams(self, strs):
        dic = collections.defaultdict(list)

        for s in strs:
            dic[str(sorted(s))].append(s)

        return dic.values()

        