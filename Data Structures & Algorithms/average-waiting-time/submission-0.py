class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        total = 0
        
        # for first customer only
        total += customers[0][1]
        time_ended = customers[0][0] + customers[0][1]

        for i in range(1, len(customers)):
            arrival = customers[i][0]
            time = customers[i][1]
            
            # in this case, the customer is waiting from last order so chef cannot prepare straight away
            if time_ended - arrival > 0:
                total += ((time_ended - arrival) + time)
                time_ended += time
            # otherwise, chef can start preparing straight away
            else:
                total += time
                time_ended = arrival + time
                
        return total / len(customers)
