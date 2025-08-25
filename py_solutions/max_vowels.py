class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        VOWELS = set('aeiou')
        count = 0

        for i in range(k):
            if s[i] in VOWELS:
                count += 1

        max_count = count

        if k == len(s): return max_count

        for i in range(k, len(s)):
            if count == k: break

            if s[i] in VOWELS: count+=1

            if s[i-k] in VOWELS: count-=1

            max_count = max(max_count, count)

        return max_count


if __name__ == "__main__":
    s = Solution()
    print(s.maxVowels("leetcode", 3))
    print(s.maxVowels("a", 1))