from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        curr_max = 0
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        if len(nums) == 3: return max(nums[0] + nums[2], nums[1])        

        v1 = nums[0]
        v2 = nums[1]
        v3 = max(nums[0] + nums[2], nums[1])        
        v4 = 0
        for i in range(3, len(nums)):
            v4 = nums[i] + max(v1, v2)

            v1 = v2
            v2 = v3
            v3 = v4

            curr_max = max(v1, v2, v3, v4)

        return curr_max

s = Solution()
print(s.rob([2, 1, 1, 2]))
print(s.rob([1, 2, 3, 1]))
