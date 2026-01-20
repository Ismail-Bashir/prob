"""
can complete a trip with given gas and cost

"""



class Solution:
    def canComplete(self, gas: List[int], cost: List[int]):

        starting_station = 0
        total_tank = 0
        current_tank = 0


        for i in range(len(gas)):
            current_tank+= gas[i] - cost[i]
            total_tank += gas[i] - cost[i]


            if current_tank < 0:
                starting_station = i+1
                current_tank = 0


        return starting_station if total_tank >= 0 else -1