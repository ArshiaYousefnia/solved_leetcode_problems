class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}

        for i in strs:
            key = "".join(sorted(i))
            val = a.get(key)

            if val == None:
                val = []
            
            val.append(i)

            a[key] = val

        out = []
        for key in a:
            out.append(a[key])

        return out 