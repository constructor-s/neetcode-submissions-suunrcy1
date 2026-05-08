class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::stack<int> s;
        for (auto item : tokens) {
            if (item == "+" || 
                item == "-" || 
                item == "*" || 
                item == "/") {
                auto o2 = s.top(); s.pop();
                auto o1 = s.top(); s.pop();
                if (item == "+") s.push(o1 + o2);
                if (item == "-") s.push(o1 - o2);
                if (item == "*") s.push(o1 * o2);
                if (item == "/") s.push(o1 / o2);
            } else {
                s.push(std::stoi(item));
            }
        }
        return s.top();
    }
};
