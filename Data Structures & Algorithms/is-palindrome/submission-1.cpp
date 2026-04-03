class Solution {
public:
    bool isPalindrome(string s) {
        if (s.length() <= 1) return true;
        if (!std::isalnum(s[0])) return isPalindrome(s.substr(1, s.length() - 1));
        if (!std::isalnum(s.back())) return isPalindrome(s.substr(0, s.length() - 1));
        return std::tolower(s[0]) == std::tolower(s.back()) && isPalindrome(s.substr(1, s.length() - 2));
    }
};
