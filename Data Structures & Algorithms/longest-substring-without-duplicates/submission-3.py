class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sequence = []
        maximum = 0
        for i in range(len(s)):
            if s[i] not in sequence:
                sequence.append(s[i])
            else:
                sequence = sequence[sequence.index(s[i]) + 1: ] + [s[i]]
            maximum = max(maximum, len(sequence))
        return maximum

        
        