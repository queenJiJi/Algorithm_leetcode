class Solution(object):
    def combine(self, n, k):
        def backtrack(start, cur, result):
            if len(cur) == k:
                result.append(cur[:])
                return

            for i in range(start, n+1):
                cur.append(i)
                backtrack(i+1,cur,result)
                cur.pop()

            return result

        return backtrack(1,[],[])



        