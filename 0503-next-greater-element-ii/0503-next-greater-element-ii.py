class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        out = [-1] * l
        stack = []

        for i in range(l * 2):
            j = i % l
            while stack and nums[stack[-1]] < nums[j]:
                idx = stack.pop()
                out[idx] = nums[j]
            stack.append(j)
        
        return out