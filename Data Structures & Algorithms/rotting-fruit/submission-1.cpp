#define ROTTEN 2
#define FRESH 1

std::vector<std::pair<int, int>> DIRECTIONS = {{0, +1}, {0, -1}, {-1, 0}, {+1, 0}};

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        struct Item {
            int depth;
            int y;
            int x;
        };
        std::queue<Item> q;
        for (int y = 0; y < grid.size(); ++y) {
            for (int x = 0; x < grid[y].size(); ++x) {
                if (grid[y][x] == ROTTEN) {
                    q.push({0, y, x});
                }
            }
        }
        
        int max_depth = 0;
        while (!q.empty()) {
            auto [depth, y, x] = q.front();
            q.pop();
            max_depth = depth;
            // std::cout << depth << ' ' << y << ' ' << x << '\n';

            for (const auto & [dx, dy] : DIRECTIONS) {
                int x_ = x + dx;
                int y_ = y + dy;
                // std::cout << y_ << ' ' << x_ << '\n';
                if (0 <= y_ && y_ < grid.size() && 0 <= x_ && x_ < grid[y_].size() && grid[y_][x_] == FRESH) {
                    grid[y_][x_] = ROTTEN;
                    q.push({depth + 1, y_, x_});
                }
            }
        }

        for (int y = 0; y < grid.size(); ++y) {
            for (int x = 0; x < grid[y].size(); ++x) {
                if (grid[y][x] == FRESH) {
                    return -1;
                }
            }
        }

        return max_depth;
    }
};
