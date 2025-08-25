class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)

            if max_area < current_area:
                max_area = current_area
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                right -= 1

        return max_area


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    print(s.maxArea(height))
