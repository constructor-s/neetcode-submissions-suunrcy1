class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> part;
        part.reserve(s.size());
        dfs(0, s, part, res);
        return res;
    }
private:
    void dfs(
        size_t i, 
        const string &s,
        vector<string> &part,
        vector<vector<string>> &res
    ) {
        if (i == s.size()) {
            res.push_back(part);
            return;
        }

        for (size_t j = i + 1; j <= s.size(); ++j) {
            if (is_pali(string_view(s).substr(i, j - i))) {
                part.push_back(s.substr(i, j - i));
                dfs(j, s, part, res);
                part.pop_back();
            }
        }
    }
    bool is_pali(std::string_view s) const {
        if (s.empty()) return true;
        auto l = s.begin();
        auto r = s.end() - 1; // Offset from past-the-end element
        while (l < r) {
            if (*l != *r) return false;
            l++;
            r--;
        }
        return true;
    }
};
