class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a = 0

        for i in nums:
            a = a ^ i
        
        a = a & (-a)

        b, c = 0, 0

        for i in nums:
            if a & i == 0:
                b = b ^ i
            else:
                c = c ^ i
        
        return [b, c]
        