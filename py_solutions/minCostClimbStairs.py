from typing import List

class Solution:    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = []
        
        dp.append(cost[0])
        dp.append(cost[1])

        for i in range(2, len(cost)):
            dp.append(cost[i] + min(dp[i-1], dp[i-2]))

        return min(dp[-1], dp[-2])


if __name__ == "__main__":
    s = Solution()
    arr = [10, 15, 20]
    print(arr)
    print(s.minCostClimbingStairs(arr))
