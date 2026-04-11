class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = {}
        res = 0

        for ch in s: # O(n)
            if ch in hm:
                hm[ch] += 1
                
                if hm[ch] % 2 == 0:
                    res += 2
            else:
                hm[ch] = 1                

        for ch in s:
            if hm[ch] % 2 != 0:
                res+=1
                return res

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abccccdd"))
