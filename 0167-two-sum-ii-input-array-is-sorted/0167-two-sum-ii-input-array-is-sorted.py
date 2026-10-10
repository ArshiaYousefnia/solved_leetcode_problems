class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1

        while (i != j):
            result = numbers[i] + numbers[j]

            if result == target:
                return [i + 1, j + 1]
            elif result < target:
                i += 1
            else:
                j -= 1
        
        return [0, 0]