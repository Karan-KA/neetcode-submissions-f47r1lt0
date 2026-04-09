from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        left = 0
        res = []
        queue = deque()

        for i in range(len(nums)):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)


            if i - left + 1 > k:
                left += 1

            
            if queue[0] < left:
                queue.popleft()

            if i - left + 1 == k:  
                res.append(nums[queue[0]])
        return res
        