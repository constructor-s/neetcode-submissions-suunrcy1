class Solution {
private:
    static constexpr int EMPTY = 0;
    static constexpr int FRESH = 1;
    static constexpr int ROTTEN = 2;
    static constexpr std::array<std::pair<int, int>, 4> DIRECTIONS{
        {{0, +1}, {0, -1}, {-1, 0}, {+1, 0}}
    };
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int fresh_count = 0;
        std::queue<int> q;
        for (int y = 0; y < m; ++y) {
            for (int x = 0; x < n; ++x) {
                if (grid[y][x] == ROTTEN) {
                    q.push(y * n + x);
                } else if (grid[y][x] == FRESH) {
                    ++fresh_count;
                }
            }
        }
        
        int depth = 0;
        for (; !q.empty(); ) {
            for (int j = 0, qs = q.size(); j < qs; ++j) {
                int i = q.front();
                q.pop();
                int y = i / n;
                int x = i % n;

                for (const auto & [dx, dy] : DIRECTIONS) {
                    int x_ = x + dx;
                    int y_ = y + dy;
                    // std::cout << y_ << ' ' << x_ << '\n';
                    if (0 <= y_ && y_ < grid.size() && 0 <= x_ && x_ < grid[y_].size() && grid[y_][x_] == FRESH) {
                        grid[y_][x_] = ROTTEN;
                        q.push(y_ * n + x_);
                        --fresh_count;
                    }
                }
            }
            if (!q.empty()) ++depth;
        }

        return fresh_count ? -1 : depth;
    }
};
