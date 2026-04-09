class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strs_map = defaultdict(list)


        for word in strs:
            strs_map["".join(sorted(word))].append(word)
            
        return list(strs_map.values())
