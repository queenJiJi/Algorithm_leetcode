class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        answer = []

        def backtrack(start, tmp):
            if len(tmp) == k:
                answer.append(tmp[:])
                return

            for i in range(start,n+1):
                tmp.append(i)
                backtrack(i+1,tmp)
                tmp.pop()

        backtrack(1,[])
        return answer
