class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        div = 1

        div = 10 ** (len(str(x)) - 1)

        
        
        while x > 1:
            print(div, x)
            print('x // div = ', x // div)
            print('x % 10 = ', x % 10)

            if x // div != x % 10:
                return False
            
            div //= 10

            if div == 0:
                return True

            x = (x // 10) % div
            div //= 10
        
        return True
            


s = Solution()
print(s.isPalindrome(454))
