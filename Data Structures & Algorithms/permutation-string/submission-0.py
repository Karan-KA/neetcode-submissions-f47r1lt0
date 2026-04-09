class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0
        hashmap_s1 = {}
        hashmap_s2 = {}

        for i in s1:

            hashmap_s1[i] = hashmap_s1.get(i, 0) + 1

        for i in range(len(s2)):

            hashmap_s2[s2[i]] = hashmap_s2.get(s2[i], 0) + 1
            

            if i-left+1 > len(s1):
                hashmap_s2[s2[left]] -= 1
                if hashmap_s2[s2[left]] == 0:
                    hashmap_s2.pop(s2[left])
                left+=1

            if i-left+1 == len(s1) and hashmap_s1 == hashmap_s2:
                return True

            

        return False