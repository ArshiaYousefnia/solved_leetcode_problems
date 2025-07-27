class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        n = len(nums)
        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            a = nums[i]
            left = i + 1
            right = n - 1

            while left < right:
                sum = a + nums[left] + nums[right]

                if (sum > 0):
                    right -= 1
                elif (sum < 0):
                    left += 1
                else:
                    out.append([a, nums[left], nums[right]])
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                    
                    left += 1
                    right -= 1

        return out

        