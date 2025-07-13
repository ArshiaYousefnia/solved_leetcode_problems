from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = defaultdict(int)
        max_len = 0
        left = 0

        for right in range(len(s)):
            occ[s[right]] += 1

            while len(occ.keys()) != (right - left + 1):
                occ[s[left]] -= 1
                if occ[s[left]] == 0:
                    del occ[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

            