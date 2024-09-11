class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, p in flights:
            graph[u].append((v, p))

        # To store the best prices to reach each node
        best_price = [float('inf')] * n
        best_price[src] = 0

        # BFS queue, storing (current node, total cost, stops used)
        queue = deque()
        queue.append( (src,0,0) )
        while queue:
            current_node, current_price, stops = queue.popleft()

            # If we've used more than k stops, skip further processing
            if stops > k:
                continue

            # Explore neighbors
            for neighbor, price in graph[current_node]:
                new_price = current_price + price

                # Only proceed if the new price is cheaper than previously known
                if new_price < best_price[neighbor]:
                    best_price[neighbor] = new_price
                    queue.append((neighbor, new_price, stops + 1))

        # If the best price to reach the destination is still infinity, return -1
        return best_price[dst] if best_price[dst] != float('inf') else -1