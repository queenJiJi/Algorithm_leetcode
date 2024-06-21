class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        text1_len_lg = len(text1)+1
        text2_len_lg = len(text2)+1

        dp = [[0]* text2_len_lg for _ in range(text1_len_lg)]

        for i in range(1,text1_len_lg):
            for j in range(1,text2_len_lg):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[i][j]
                
        