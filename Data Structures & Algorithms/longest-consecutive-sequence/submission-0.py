class Solution:
    def longestConsecutive(self, nums):
        
        nums = set(nums)

        maximum = 0

        for num in nums:
            current = num
            length = 1
            if num-1 not in nums: 
                while current + 1 in nums:
                    current += 1
                    length+=1
                maximum = max(maximum, length)
        return maximum