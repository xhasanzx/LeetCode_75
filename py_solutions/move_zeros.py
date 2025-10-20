class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for index, number in enumerate(nums):
            if number == 0:
                nums.pop(index)
                nums.append(0)


if __name__ == "__main__":
    s = Solution()
    s.moveZeroes(nums=[0, 1, 0, 3, 12])
