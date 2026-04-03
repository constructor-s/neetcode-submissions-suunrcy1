class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;

        auto m = std::unordered_map<char, int>();
        for (size_t i = 0; i < s.length(); ++i) {
            m[s[i]] += 1;
            m[t[i]] -= 1;
        }

        for (auto const& pair : m) {
            if (pair.second != 0) return false;
        }

        return true;
    }
};
