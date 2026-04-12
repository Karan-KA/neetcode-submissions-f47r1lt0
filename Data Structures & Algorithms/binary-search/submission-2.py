class Solution:
    
    def search(self, nums: List[int], target: int, offset =0) -> int:

            middle = (len(nums) // 2)

            if not nums:
                return -1

            if nums[middle] == target:
                return middle + offset

            elif nums[middle] < target:
                return self.search(nums[middle+1:], target, offset = middle+1)
            elif nums[middle] > target:
                return self.search(nums[0: middle], target, offset)


        