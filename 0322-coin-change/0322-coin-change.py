from collections import deque
class Solution(object):
    def coinChange(self, coins, amount):
        q= deque()
        q.append((amount,0)) # 할당가격,사용 코인
        visited= set()
        while q:
            cur_amount, num_coin = q.popleft()  
            visited.add(cur_amount)

            if cur_amount == 0:
                return num_coin
            
            for coin in coins:
                next_amount = cur_amount - coin
                if next_amount not in visited and next_amount >=0:
                    q.append((next_amount,num_coin+1))
                    visited.add(next_amount)
            
        return -1