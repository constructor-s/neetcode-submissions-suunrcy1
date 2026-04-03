class Solution {
public:
    bool isPalindrome(string s) {
        std::string filtered; // To store the filtered version of the string

        // Step 1: Normalize the string
        for (char c : s) {
            if (std::isalnum(c)) { // Check if the character is alphanumeric
                filtered += std::tolower(c); // Convert to lowercase and append
            }
        }

        // Step 2: Check if the filtered string is a palindrome
        int left = 0;
        int right = filtered.size() - 1;
        
        while (left < right) {
            if (filtered[left] != filtered[right]) {
                return false; // Not a palindrome
            }
            left++;
            right--;
        }
        return true; // It is a palindrome
    }
};
