class Solution {
public:
    std::vector<std::vector<std::string>> partition(std::string s) {
        std::vector<std::vector<std::string>> res;
        std::vector<std::string_view> part;
        part.reserve(s.size());
        
        std::string_view sv(s);
        dfs(0, sv, part, res);
        return res;
    }

private:
    void dfs(
        size_t i, 
        std::string_view sv,
        std::vector<std::string_view> &part,
        std::vector<std::vector<std::string>> &res
    ) {
        if (i == sv.size()) {
            // Materialize string heap objects ONLY when the schema is fully validated
            std::vector<std::string> complete_partition;
            complete_partition.reserve(part.size());
            for (const auto& view : part) {
                complete_partition.emplace_back(view);
            }
            res.push_back(std::move(complete_partition));
            return;
        }

        for (size_t j = i + 1; j <= sv.size(); ++j) {
            std::string_view sub = sv.substr(i, j - i);
            if (is_pali(sub)) {
                part.push_back(sub);     // O(1) zero-allocation push
                dfs(j, sv, part, res);   // Continue exploration
                part.pop_back();        // O(1) zero-allocation pop
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
