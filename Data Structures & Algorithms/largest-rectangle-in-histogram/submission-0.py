class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0

        for i in range(len(heights)):
            current_height = heights[i]
            while stack and heights[stack[-1]] > current_height:
                height = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = (i - stack[-1]) -1

                area = width * height

                max_area = max(max_area, area)
            stack.append(i)

        while stack:
            n = len(heights) 
            if stack:
                height = heights[stack.pop()]
                if not stack:
                    width = n
                else:
                    width =  n - stack[-1] - 1

                area = height * width

                max_area = max(max_area, area)

        return max_area

 


        