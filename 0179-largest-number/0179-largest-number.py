class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        out = ""

        n = len(nums)

        for i in range(n):
            num_max = nums[0]
            index_max = 0

            for j in range(1, len(nums)):
                if self.compare(nums[j], num_max):
                    num_max = nums[j]
                    index_max = j
            
            out += str(num_max)
            nums.pop(index_max)
        
        return str(int(out))


    def compare(self, a: int, b: int) -> bool:
        str_a = str(a)
        str_b = str(b)
        
        return int(str_a + str_b) > int(str_b + str_a)


