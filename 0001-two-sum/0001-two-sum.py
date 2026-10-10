class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums = [(j, i) for i, j in enumerate(nums)]
        nums.sort()

        start = 0
        end = len(nums) - 1

        while (start < end):
            result = nums[start][0] + nums[end][0]

            if result == target:
                return [nums[start][1], nums[end][1]]
            
            if result < target:
                start = start + 1
            else:
                end = end - 1
        
        return [-1, -1]
        
