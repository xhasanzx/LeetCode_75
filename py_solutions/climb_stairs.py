class Solution:
    history = {}
    def climbStairs(self, n: int) -> int:        
        if n == 1: return 1
        if n == 2: return 2
        if n in self.history:
            return self.history[n]
        else: 
            self.history[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.history[n]
