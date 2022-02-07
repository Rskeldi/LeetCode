# Given a string s, find the length of the longest substring without
# repeating characters.


class Solution:
    def __init__(self):
        super().__init__()
        self.count = 0

    def lengthOfLongestSubstring(self, s: str) -> int:
        for i in range(len(s)):
            strings = []
            for j in s[i:]:
                if j not in strings:
                    strings.append(j)
                else:
                    break
            if len(strings) > self.count:
                self.count = len(strings)
        return self.count
