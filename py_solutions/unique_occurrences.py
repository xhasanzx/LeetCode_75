class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        mapping = {}
        for num in arr:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1

        occurrences = list(mapping.values())
        occurrences.sort()

        for i in range(len(occurrences) - 1):
            if occurrences[i] == occurrences[i + 1]:
                return False

        return True