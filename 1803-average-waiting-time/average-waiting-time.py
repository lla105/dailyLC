class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        if not customers:
            return 0
        # prev_finish = customers[0][1] + customers[0][0]
        prev_finish = 0
        total_waited = []

        if len(customers) == 1:
            return prev_finish
        
        for i in range(len(customers)):
            cur_arrive = customers[i][0]
            tempwaited = customers[i][1] 
            # print(f'{i} )')
            if prev_finish >= cur_arrive:
                # print(f'    clash!')
                tempwaited += prev_finish - cur_arrive
                # cur_arrive = prev_finish
            # print(f'    cur_arrive: {cur_arrive}, waited:{tempwaited}')
            
            prev_finish = cur_arrive + tempwaited
            total_waited.append(tempwaited)
            # print(f'    finished at:{prev_finish}')


        total_sum = sum(total_waited)
        answer = total_sum / len(customers)
        return answer