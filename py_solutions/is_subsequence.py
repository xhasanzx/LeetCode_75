class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        s_index = 0
        t_index = 0

        for t_index in range(len(t)):
            print(f"{s[s_index]} Vs {t[t_index]}")

            if s[s_index] == t[t_index]:
                s_index += 1

            if s_index == len(s):
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence("abc", "acbbszac"))
