class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_map = {}
        ans = []
        for num in nums:
            nums_map[num] = nums_map.get(num, 0) + 1

        bucket_list = [[] for i in range(len(nums)+1)]
        
        for num, frq in nums_map.items():
            bucket_list[frq].append(num)

        for i in range(len(bucket_list)-1,0,-1):
            for num in bucket_list[i]:
                ans.append(num)
                if len(ans) == k: 
                    return ans
        