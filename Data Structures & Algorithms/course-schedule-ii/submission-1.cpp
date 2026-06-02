class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        // Indegree-based topological sort
        std::vector<std::unordered_set<int>> prereqs(numCourses);
        std::vector<std::vector<int>> satisfies(numCourses);
        for (const auto &item : prerequisites) {
            prereqs[item[0]].insert(item[1]);
            satisfies[item[1]].push_back(item[0]);
        }

        std::queue<int> q;
        for (int i = 0; i < numCourses; ++i) {
            if (prereqs[i].empty()) q.push(i);
        }

        std::vector<int> path; path.reserve(numCourses);
        while (!q.empty()) {
            int curr = q.front(); q.pop(); path.push_back(curr);
            for (int next : satisfies[curr]) {
                prereqs[next].erase(curr);
                if (prereqs[next].empty()) {
                    q.push(next);
                }
            }
        }

        // return (path.size() == numCourses) ? path : {};
        if (path.size() == numCourses) {
            return path;
        } else {
            return {};
        }
    }
};
