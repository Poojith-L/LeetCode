class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Stores characters and their latest index
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1  # Move left pointer
            char_index[s[right]] = right  # Update current character index
            max_len = max(max_len, right - left + 1)

        return max_len