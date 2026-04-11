class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "*":
                stack.append(ch)
            else:
                stack.pop()

        result = "".join(stack)
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.removeStars("leet**cod*e"))
    print(solution.removeStars("erase*****"))

