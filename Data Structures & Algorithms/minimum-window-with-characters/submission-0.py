class Solution:
    def minWindow(self, s: str, t: str) -> str:

        left = 0
        min_length = float("inf") # infinity
        hashmap_t = {}
        hashmap_s = {}
        have = 0

        for i in t:
            hashmap_t[i] =  hashmap_t.get(i, 0) + 1

        for i in range(len(s)):
            hashmap_s[s[i]] = hashmap_s.get(s[i], 0) + 1

            if s[i] in hashmap_t and hashmap_s[s[i]] == hashmap_t[s[i]]:
                have+=1

            while have == len(hashmap_t):

                if (i - left +  1)  < min_length:
                    start =  left
                    min_length = i - left +  1
                hashmap_s[s[left]] -= 1

                if s[left] in hashmap_t and hashmap_s[s[left]] < hashmap_t[s[left]]:
                    have-=1

                left+=1
        return s[start:start+min_length] if min_length != float("inf") else ""


        