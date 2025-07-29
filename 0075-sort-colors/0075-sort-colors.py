class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buck = [0, 0, 0]
        for i in nums:
            buck[i] += 1
        
        for i in range(len(nums)):
            if i < buck[0]:
                nums[i] = 0
            elif i < buck[0] + buck[1]:
                nums[i] = 1
            else:
                nums[i] = 2

        