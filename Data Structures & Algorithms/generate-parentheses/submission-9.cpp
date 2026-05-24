class Solution {
public:
    vector<string> generateParenthesis(int n) {
        if (n == 0) return {""};

        std::vector<std::string> res;

        std::stack<std::pair<std::string, size_t>> sta;
        sta.push({"("s, 1});
        
        while (!sta.empty()) {
            auto [s, l_count] = std::move(sta.top());
            sta.pop();
            const auto r_count = s.size() - l_count;

            if (l_count == n && r_count == n) res.push_back(std::move(s));
            else {
                if (l_count < n) sta.push({s + '(', l_count + 1});
                if (l_count > r_count) sta.push({s + ')', l_count});
            }
        }

        return res;
    }
};
