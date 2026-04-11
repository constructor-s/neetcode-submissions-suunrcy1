import bisect

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(src, visited=None):
            if visited is None:
                visited = set()

            if len(visited) == len(tickets):
                return [src]

            for dest, i in tickets_by_source.get(src, []):
                if i not in visited:
                    new_visited = set(visited)
                    new_visited.add(i)
                    path = dfs(dest, new_visited)
                    if path is not None:
                        return [src] + path

            return None

        tickets_by_source = {}
        for i, (src, dest) in enumerate(tickets):
            if src not in tickets_by_source:
                tickets_by_source[src] = [(dest, i)]
            else:
                bisect.insort(tickets_by_source[src], (dest, i))

        return dfs("JFK")
