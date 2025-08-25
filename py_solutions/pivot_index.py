class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = 0
        total_sum = sum(nums)

        for i, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.pivotIndex([1,7,3,6, 5,6]))