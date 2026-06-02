class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        // Indegree-based topological sort
        std::vector<int> nPrereqs(numCourses);
        std::vector<std::vector<int>> satisfies(numCourses);
        for (const auto &item : prerequisites) {
            ++(nPrereqs[item[0]]);
            satisfies[item[1]].push_back(item[0]);
        }

        std::queue<int> q;
        for (int i = 0; i < numCourses; ++i) {
            if (nPrereqs[i] == 0) q.push(i);
        }

        std::vector<int> path; path.reserve(numCourses);
        while (!q.empty()) {
            int curr = q.front(); q.pop(); path.push_back(curr);
            for (int next : satisfies[curr]) {
                --(nPrereqs[next]);
                if (nPrereqs[next] == 0) {
                    q.push(next);
                }
            }
        }

        return (path.size() == numCourses) ? path : vector<int>{};
    }
};
