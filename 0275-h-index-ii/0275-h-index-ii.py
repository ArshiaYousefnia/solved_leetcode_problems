class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        i = 0
        j = n

        while i < j:
            middle = (i + j) // 2
            c = citations[middle]

            if c >= (n - middle):
                j = middle
            else:
                i = middle + 1
        
        return n - j
        