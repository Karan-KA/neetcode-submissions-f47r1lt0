class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []

        for temp in range(len(temperatures) - 1, -1, -1):
            nxtgreatertemp = 0
            while stack and temperatures[temp] >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                nxtgreatertemp = stack[-1] - temp
        
            stack.append(temp)

            res.append(nxtgreatertemp)

        return  res[::-1]

