class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heapq.heapify_max(stones)

        while not len(stones) <= 1:
            value1 = heapq.heappop_max(stones)
            value2 = heapq.heappop_max(stones)
            result = value1 - value2
            if result > 0:
                heapq.heappush_max(stones, result)
        return 0 if not stones else stones[0]
        