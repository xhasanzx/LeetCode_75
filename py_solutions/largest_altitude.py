class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitudes = [0]
        for i in range(1, len(gain)+1):
            altitudes.append(altitudes[-1] + gain[i-1])
        print(altitudes)
        return max(max(altitudes), 0)


if __name__ == '__main__':
    s = Solution()
    print(s.largestAltitude([1, 3, 5, 7]))
