class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adj(n);
        for (auto e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        vector<bool> visited(n, false);
        int components = 0;
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                dfs(i, adj, visited);
                ++components;
            }
        }
        return components;
    }

    void dfs(int i, const vector<vector<int>>& adj, vector<bool>& visited) {
        stack<int> s;
        s.push(i);
        // cout << "start " << i << '\n';
        visited[i] = true;
        while (s.size()) {
            int i = s.top();
            // cout << "found " << i << '\n';
            s.pop();
            visited[i] = true;
            for (int e : adj[i]) {
                if (!visited[e]) {
                    visited[e] = true;
                    s.push(e);
                }
            }
        }
    }
};
