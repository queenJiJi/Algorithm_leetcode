from itertools import permutations
class Solution(object):
    def getPermutation(self, n, k):
        arr= list(permutations(range(1,n+1),n))

        for i in range(1,len(arr)+1):
            if i==k:
                break
        answer = ''
        for i in arr[i-1]:
            answer+=str(i)
        return answer