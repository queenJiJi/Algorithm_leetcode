from itertools import permutations
class Solution(object):
    def getPermutation(self, n, k):
        return ''.join(map(str, list(permutations(range(1,n+1),n))[k-1]))
        