class Solution:
    def maxArea(self, height: List[int]) -> int:
        Max = 0
        n = len(height)
        left = 0
        right = n - 1

        while left < right:
            Max = max(Max, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return Max

