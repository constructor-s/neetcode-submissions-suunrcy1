class Solution {
public:
    vector<vector<string>> partition(string s) {
        string_view sv(s);
        vector<vector<string>> res;

        // DFS
        vector<Item> sta = {
            {0, {}}
        };
        while (!sta.empty()) {
            auto [curr_index, parts] = move(sta.back());
            sta.pop_back();

            if (curr_index == sv.size()) {
                vector<string> partitions;
                partitions.reserve(parts.size());
                for (const auto& view : parts) {
                    partitions.emplace_back(view);
                }
                res.push_back(move(partitions));
            } else {
                for (size_t r = curr_index; r < sv.size(); ++r) {
                    if (is_pali(sv.substr(curr_index, r - curr_index + 1))) {
                        vector<string_view> new_parts(parts);
                        new_parts.push_back(sv.substr(curr_index, r - curr_index + 1));
                        sta.push_back({r + 1, new_parts});
                    }
                }
            }
        }

        return res;
    }
private:
    struct Item {
        size_t curr_index;
        vector<string_view> parts;
    };
    // bool is_pali(const string_view &s) {
    //     auto l = s.begin();
    //     auto r = s.end();
    //     while (l < r) {
    //         if (*l != *r) return false;
    //         l++;
    //         r--;
    //     }
    //     return true;
    // }
    bool is_pali(string_view sub) {
        if (sub.empty()) return true;
        size_t l = 0;
        size_t r = sub.size() - 1;
        while (l < r) {
            if (sub[l] != sub[r]) return false;
            l++; // Fix: Missing iterator increments
            r--; // Fix: Missing iterator decrements
        }
        return true;
    }
};
