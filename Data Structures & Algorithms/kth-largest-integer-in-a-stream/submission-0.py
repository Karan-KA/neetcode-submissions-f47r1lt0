import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.dupnums = nums.copy()

    def add(self, val: int) -> int:

        heapq.heappush_max(self.nums,val)
        heapq.heappush_max(self.dupnums,val)

        heapq.heapify_max(self.nums)
        heapq.heapify_max(self.dupnums)

        n = len(self.nums)
        sortednum = []
        for i in range(n):
            value = heapq.heappop_max(self.dupnums)
            sortednum.append(value)

        self.dupnums = self.nums.copy()
        value = sortednum[self.k-1]
        sortednum = []
        return value


        
