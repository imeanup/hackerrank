class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        pq = []
        for i in range(candidates):
            heappush(pq, (costs[i], 0))
        for i in range(max(candidates, n - candidates), n):
            heappush(pq, (costs[i], 1))

        answer = 0
        next_head, next_tail = candidates, n - 1 - candidates 

        for _ in range(k):
            cost, i = heappop(pq)
            answer += cost
            if next_head <= next_tail:
                if i == 0:
                    heappush(pq, (costs[next_head], 0))
                    next_head += 1
                else:
                    heappush(pq, (costs[next_tail], 1))
                    next_tail -= 1

                    
        return answer
