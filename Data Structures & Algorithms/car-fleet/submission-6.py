class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = map(list, zip(*sorted(zip(position, speed), reverse=True)))
        print(position)
        print(speed)
        N = len(position)
        counter = 0
        head = 0
        while head < N:
            counter += 1
            timeNeededForHeadToArrive = (target-position[head]) / speed[head]
            print("head:", timeNeededForHeadToArrive)
            i = head + 1
            while i < N:
                timeNeededForIToArrive = (target-position[i]) / speed[i]
                print("i:", timeNeededForIToArrive)
                if timeNeededForIToArrive > timeNeededForHeadToArrive:
                    break
                i += 1
            head = i
        return counter
            
    # def carFleet(self, target, position, speed):
    #     cars = sorted(zip(position, speed), reverse=True)
    #     fleets = 0
    #     max_time = 0

    #     for p, s in cars:
    #         time = (target - p) / s
    #         if time > max_time:
    #             fleets += 1
    #             max_time = time

    #     return fleets