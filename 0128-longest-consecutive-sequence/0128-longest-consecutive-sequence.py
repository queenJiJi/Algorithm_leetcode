class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums = sorted(set(nums)) # 중복제거 + 정렬

        cnt = 1
        answer = 1

        for i in range(len(nums)-1):

            if nums[i+1]-nums[i]== 1:
                cnt+=1
                # print('i',i,cnt)
            else:
                answer = max(cnt, answer)
                cnt= 1 # 연속성 끊기면 다시 1로 초기화
        answer = max(cnt, answer)

        # print(answer)
        return answer
        