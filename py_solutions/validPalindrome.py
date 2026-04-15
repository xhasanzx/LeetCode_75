class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        lower_str = s.lower()

        while left < right:
            if not lower_str[left].isalnum():
                left = left + 1
                continue
            if not lower_str[right].isalnum():
                right = right - 1
                continue

            if lower_str[left] == lower_str[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
    
