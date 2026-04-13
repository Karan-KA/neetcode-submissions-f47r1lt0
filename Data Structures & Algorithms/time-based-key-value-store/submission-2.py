from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.dictionary = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        dict_val = self.dictionary.get(key, [])
        if not dict_val:
            return ""

        low, high = 0, len(dict_val) - 1
        res = ""  

        while low <= high:
            mid = (low + high) // 2
            if dict_val[mid][0] == timestamp:
                return dict_val[mid][1] 
            elif dict_val[mid][0] < timestamp:
                res = dict_val[mid][1]  
                low = mid + 1
            else:
                high = mid - 1

        return res

                



        
