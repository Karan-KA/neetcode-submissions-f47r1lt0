class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0
        j = len(numbers) - 1


        while i < j:
            sm =  numbers[i] + numbers[j]

            if sm == target:
                return [i+1,j+1]

            elif sm < target:
                i+=1
            else:
                j-=1
        return sm
        