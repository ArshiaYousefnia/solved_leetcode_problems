from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        table = defaultdict(int)

        for i in range(len(s) - 9):
            string = s[i:i + 10]

            if table[string] <= 1:
                table[string] += 1

        out = []
        for i, val in table.items():
            if val > 1:
                out.append(i)
        
        return out
        