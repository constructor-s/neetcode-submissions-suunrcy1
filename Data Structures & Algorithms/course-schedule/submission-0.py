class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph 
        # if there is no cycle in the graph, return True
        adj = [list() for _ in range(numCourses)]
        for first, second in prerequisites:
            adj[second].append(first)
            # node[i] are the prereqs required for course i

        def has_cycle(curr, adj, visited):
            for n in adj[curr]:
                if n in visited:
                    return True
                visited_ = set(visited)
                visited_.add(n)
                if has_cycle(n, adj, visited_):
                    return True

            return False

        for i in range(len(adj)):
            if has_cycle(i, adj, visited=set()):
                return False # cannot finish, has cycle
        return True
