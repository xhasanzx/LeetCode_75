class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # 12.75
    print(s.findMaxAverage([-1], 1))  # -1
    print(s.findMaxAverage([4, 0, 4, 3, 3], 1))  # 4.0
    print(s.findMaxAverage([4, 2, 1, 3, 3], 2))  # 3.0
