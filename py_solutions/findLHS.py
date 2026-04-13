from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:        
        lhs = 0
        occ = Counter(nums)
        # occ = {}
        # for num in nums:
        #     if num in occ:
        #         occ[num] += 1
        #     else:
        #         occ[num] = 1
        #     if num - 1 in occ:
        #         lhs = max(lhs, occ[num] + occ[num-1])
        #     if num + 1 in occ:
        #         lhs = max(lhs, occ[num] + occ[num+1])
        for key in occ:
            if key - 1 in occ:
                lhs = max(lhs, occ[key] + occ[key-1])
        return lhs
    
    
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findLHS([1,3,2,2,5,2,3,7]))
