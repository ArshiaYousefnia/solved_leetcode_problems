class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurences = {}
        thresh = len(nums) / 2

        for element in nums:
            el = occurences.get(element, 0) + 1

            if el >= thresh:
                return element

            occurences[element] = el
        