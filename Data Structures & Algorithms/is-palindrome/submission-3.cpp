class Solution {
public:
    bool isPalindrome(string s) {
        auto sv = string_view(s);
        return isPalindromeSv(sv);
    }

    bool isPalindromeSv(string_view s) {
        if (s.length() <= 1) return true;
        if (!isalnum(s[0])) return isPalindromeSv(s.substr(1, s.length() - 1));
        if (!isalnum(s.back())) return isPalindromeSv(s.substr(0, s.length() - 1));
        return tolower(s[0]) == tolower(s.back()) && isPalindromeSv(s.substr(1, s.length() - 2));
    }
};
