class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        target_map = {}

        for num_idx in range(len(nums)):
            complement = target - nums[num_idx]

            if complement in target_map.keys():
                return [target_map[complement], num_idx]
            target_map[nums[num_idx]] = num_idx
        