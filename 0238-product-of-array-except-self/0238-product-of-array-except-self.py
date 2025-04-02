class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        a = n * [1]

        p_left = 1
        p_right = 1
        for i in range(n):
            num_1 = nums[i]
            num_2 = nums[n - 1 - i]

            a[i] *= p_left
            p_left *= num_1

            a[n - 1 - i] *= p_right
            p_right *= num_2

        return a
        