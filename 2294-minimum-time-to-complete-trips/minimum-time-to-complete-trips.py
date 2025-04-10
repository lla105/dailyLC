class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        i = 0 # time (ith hour)
        trips_arr = []
        # 1: trips_arr = [1,0,0] = 1
        # 2: trips_arr = [2,1,0] = 3
        # 3: trips_arr = [3,1,1] = 5
        # i%time[j] == 0 (except for time[j]==1) -> if true, +1
        # n = len(time)
        #
        l = 0
        r = totalTrips * min(time) # 5*1 = 5 = r
        m= 0
        while l<r: # 3<3
            m = (l+r) // 2 # m is amount of hour = 4
            trips = 0
            for i in range(len(time)) :# time=[1,2,3]
                trips += (m // time[i]) 
            if trips >= totalTrips:
                r = m 
            elif trips < totalTrips:
                l = m + 1
        return l

        return 0
