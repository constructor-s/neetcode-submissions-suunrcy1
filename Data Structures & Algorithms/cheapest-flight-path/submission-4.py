class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        for fr, to, price in flights:
            if fr not in adj:
                adj[fr] = [(fr, to, price)]
            else:
                adj[fr].append((fr, to, price))

        prev_cost = [float("inf")] * n
        prev_cost[src] = 0
        for _ in range(k+1):
            cost = prev_cost.copy()

            for i in range(n):
                if prev_cost[i] < float("inf"):
                    for fr, to, price in adj.get(i, []):
                        cost[to] = min(cost[to], prev_cost[i] + price)
                        # print(_, fr, to, price, cost)
            
            prev_cost = cost.copy()
        
        if prev_cost[dst] == float("inf"):
            return -1
        else:
            return prev_cost[dst]
