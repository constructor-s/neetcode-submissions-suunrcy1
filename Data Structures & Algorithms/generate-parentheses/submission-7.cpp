class Solution {
public:
    vector<string> generateParenthesis(int n) {
        if (n == 0) return {};

        std::vector<std::string> res;

        auto init = std::make_tuple(std::string("("), 1);
        std::stack<decltype(init)> sta;
        sta.push(init);
        while (!sta.empty()) {
            auto [s, l_count] = sta.top();
            sta.pop();
            const auto r_count = s.size() - l_count;

            if (l_count == n && r_count == n) res.push_back(s);
            else {
                if (l_count < n) sta.push(std::make_tuple(s + '(', l_count + 1));
                if (l_count > r_count) sta.push(std::make_tuple(s + ')', l_count));
            }
        }

        return res;
    }
};
