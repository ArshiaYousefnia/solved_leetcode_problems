class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        map = {}
        occur = {}
        n = len(nums)
        map[nums[0]] = 1

        for i in range(1, n - 1):
            a = nums[i]

            seen_bef = {}
            for j in range(i + 1, n):
                b = nums[j]

                if b in seen_bef:
                    continue
                seen_bef[b] = 1
                
                exp = -(a + b)
                
                if exp in map:
                    can = sorted([a, b, exp])
                    g = str(can)
                    if g not in occur:
                        out.append(can)
                        occur[g] = 1
                
            if nums[i] not in map:
                map[nums[i]] = 1
            
        return out

        