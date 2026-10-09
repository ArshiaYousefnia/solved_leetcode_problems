class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        mapping = {}

        for i in nums:
            before = mapping.get(i, 0)

            if before > 0:
                return True
            
            mapping[i] = before + 1
        
        return False