class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        s_set = set()
        maximum_length = 0
        for r in range(len(s)):

            while s[r] in s_set:
                s_set.remove(s[left])
                left+= 1
                
               
            s_set.add(s[r])

            maximum_length = max(r-left+1, maximum_length)
        return maximum_length