class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::stack<int> s;
        for (const auto& c : tokens) {
            if (c.size() > 1 || std::isdigit(c[0])) {
                s.push(std::stoi(c));
            } else {
                auto o2 = s.top(); s.pop();
                auto o1 = s.top(); s.pop();
                switch (c[0]) {
                    case '+': s.push(o1 + o2); break;
                    case '-': s.push(o1 - o2); break;
                    case '*': s.push(o1 * o2); break;
                    case '/': s.push(o1 / o2); break;
                    default: break;
                }
            }
        }
        return s.top();
    }
};
