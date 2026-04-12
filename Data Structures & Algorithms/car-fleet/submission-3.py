class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse = True)
        prev_time = 0
        fleet = 0

        for pos, speed in cars:
            time = (target - pos) / speed

            if time > prev_time:
                fleet+=1
                prev_time = time

        return fleet
    
        