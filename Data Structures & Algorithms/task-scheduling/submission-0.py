class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # Intution: most frequent element heap, utilizing only frequency 
        # Queue to see when to insert that popped element back to the maxheap
        # If frequency is 0 not to append that back to queue

        time  = 0

        freq = Counter(tasks)

        freq_list = [count for count in freq.values()]

        heapq.heapify_max(freq_list)
        print(freq_list)

        q = deque()

        while freq_list or q:
            time += 1
            if freq_list:
                cnt = heapq.heappop_max(freq_list) - 1
                if cnt:
                    q.append([cnt, time + n])
                
            if q and q[0][1] == time:
                heapq.heappush_max(freq_list, q.popleft()[0])
        return time



            


        return 0
