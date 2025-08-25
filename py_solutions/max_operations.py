from collections import deque


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        dq = deque(sorted(nums))
        count = 0
        while len(dq) > 1:
            s = dq[0] + dq[-1]
            if s == k:
                dq.popleft()
                dq.pop()
                count += 1
            elif s < k:
                dq.popleft()
            else:
                dq.pop()
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.maxOperations([2, 2, 2, 3, 1, 1, 4, 1], 3))
