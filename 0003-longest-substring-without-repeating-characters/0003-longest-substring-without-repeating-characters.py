class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_positions = {}

        dp = 0

        max_dp = 0

        for i, char in enumerate(s):
            last_position = last_positions.get(char, -1)

            if i - 1 - dp < last_position:
                dp = i - last_position
            else:
                dp = dp + 1

            max_dp = max(max_dp, dp)

            last_positions[char] = i

        return max_dp