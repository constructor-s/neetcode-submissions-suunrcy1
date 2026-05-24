class Solution {
public:
    vector<string> generateParenthesis(int n) {
        std::vector<std::vector<std::string>> cache(n + 1);
        cache[0].push_back("");

        std::string temp;
        temp.reserve(2 * n);
        for (int i = 1; i < n + 1; ++i) {
            for (int l = 0; l < i; ++l) {
                const int r = i - 1 - l;

                for (const auto& left : cache[l]) {
                    temp.push_back('(');
                    temp.append(left);
                    temp.push_back(')');
                    for (const auto& right : cache[r]) {
                        temp.append(right);
                        cache[i].push_back(temp);
                        temp.erase(l*2 + 2, r*2);
                    }
                    temp.erase();
                }
            }
        }

        return cache[n];
    }
};
