


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        sorted_array = sorted(nums)

        for i in range(len(nums)):
            l =i+1
            r = len(nums) - 1

            if i > 0 and sorted_array[i-1] == sorted_array[i]:
                continue

            while l < r:

                total = sorted_array[i] + sorted_array[l] + sorted_array[r]

                if total == 0:
                    res.append([sorted_array[i], sorted_array[l], sorted_array[r]])

                    while l < r and sorted_array[l] == sorted_array[l+1]:
                        l+=1
                    while l < r and sorted_array[r] == sorted_array[r-1]:
                        r-=1
                
                    l+=1
                    r-=1
                elif total < 0:
                    l+=1
                else:
                    r-=1
        return res

            
            
        