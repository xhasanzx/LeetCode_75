class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 > a :
                if stack[-1] < -a:
                    stack.pop()
                elif stack[-1] == -a:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(a)

        return stack

if __name__ == '__main__':
    s = Solution()
    print(s.asteroidCollision([5, 10, -5]))
    print(s.asteroidCollision([3, 5, -6, 2, -1, 4]))
    print(s.asteroidCollision([8, -8]))
    print(s.asteroidCollision([-2,-2,1,-2]))