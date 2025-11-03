class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        answer = 0
        freq_hash = {}
        length = len(grid)

        # Count the frequency of each row
        for row in grid:
            row_tuple = tuple(row)
            freq_hash[row_tuple] = freq_hash.get(row_tuple, 0) + 1

        # Compare each column to stored rows
        for i in range(length):
            column = tuple(grid[j][i] for j in range(length))
            if column in freq_hash:
                answer += freq_hash[column]

        return answer


if __name__ == "__main__":
    s = Solution()
    print(s.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]), "correct answer: 1")
    print(
        s.equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]),
        "correct answer: 3",
    )
    print(s.equalPairs([[11, 1], [1, 11]]), "correct answer: 2")
    print(s.equalPairs([[13, 13], [13, 13]]), "correct answer: 4")
