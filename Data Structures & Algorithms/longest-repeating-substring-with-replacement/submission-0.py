class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        hashmap = {}
        res = 0

        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1
            if (i-left+1) - max(hashmap.values()) > k:
                hashmap[s[left]] -= 1
                left+=1
            res = max(res, i-left+1)

        return res
        