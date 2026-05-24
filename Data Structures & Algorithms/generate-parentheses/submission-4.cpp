class Solution {
public:
    vector<string> generateParenthesis(int n) {
        std::vector<std::vector<std::string>> cache(n + 1);
        cache[0].push_back("");

        for (int i = 1; i < n + 1; ++i) {
            for (int l = 0; l < i; ++l) {
                const int r = i - 1 - l;

                for (auto left : cache[l]) {
                    for (auto right : cache[r]) {
                        cache[i].push_back(
                            '(' + left + ')' + right
                        );
                    }
                }
            }
        }

        return cache[n];
    }
};
