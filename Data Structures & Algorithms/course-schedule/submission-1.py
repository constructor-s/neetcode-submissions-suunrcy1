class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [list() for _ in range(numCourses)]
        for first, second in prerequisites:
            adj[second].append(first)
            # node[i] are the prereqs required for course i

        cache = [None] * numCourses

        def has_cycle(curr, adj, visited):
            if cache[curr] is not None:
                return cache[curr]

            for n in adj[curr]:
                if n in visited:
                    cache[curr] = True
                    return True
                visited_ = set(visited)
                visited_.add(n)
                if has_cycle(n, adj, visited_):
                    cache[curr] = True
                    return True
            
            cache[curr] = False
            return False

        for i in range(len(adj)):
            if has_cycle(i, adj, visited=set()):
                return False # cannot finish, has cycle
        return True
