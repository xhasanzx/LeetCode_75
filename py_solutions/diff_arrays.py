class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2), list(set2 - set1)]


if __name__ == '__main__':
    s = Solution()
    print(s.findDifference([2,4,6], [1,2,3]))