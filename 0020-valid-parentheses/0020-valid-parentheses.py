class Solution:
    def isValid(self, s: str) -> bool:
        p = []

        for i in s:
            if i in ["{", "[", "("]:
                p.append(i)
            else:
                if len(p) == 0:
                    return False
                a = p[-1]
                if i == "}" and a != "{":
                    return False
                if i == ")" and a != "(":
                    return False
                if i == "]" and a != "[":
                    return False
                p.pop()
        
        return (len(p) == 0)      