class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s, p = s2, s1
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return False
        
        p_dict = {}

        for i in p:
            p_dict[i] = p_dict.get(i, 0) + 1

        w_dict = {}

        for i in range(len_p):
            w_dict[s[i]] = w_dict.get(s[i], 0) + 1

        if w_dict == p_dict:
            return True
        
        for i in range(1, len_s - len_p + 1):
            w_dict[s[i - 1]] = w_dict[s[i - 1]] - 1
            if w_dict[s[i - 1]] == 0:
                del w_dict[s[i - 1]]
            w_dict[s[i + len_p - 1]] = w_dict.get(s[i + len_p - 1], 0) + 1

            if w_dict == p_dict:
                return True

        return False