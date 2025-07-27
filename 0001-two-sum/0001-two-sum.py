class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        combined = zip(nums, [i for i in range(n)])
        combined = sorted(combined)

        a, b = zip(*combined)

        a = list(a)
        b = list(b)


        left = 0
        right = n - 1

        while left < right:
            sum = a[left] + a[right]

            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [b[left], b[right]]
        
        return []