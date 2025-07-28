class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1

        a = [0] * n

        for num in nums:
            g = a[num - 1]
            a[num - 1] += 1

            if g == 1:
                return num

    

        