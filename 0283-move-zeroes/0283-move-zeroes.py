class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        count = 0

        while i < n:
            if nums[i] == 0:
                nums.pop(i)
                count += 1
                n -= 1
            else:
                i += 1

        for i in range(count):
            nums.append(0)
        