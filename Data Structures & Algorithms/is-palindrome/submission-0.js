class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isAlphaNumericNoRegex(str) {
        for (let i = 0, len = str.length; i < len; i++) {
            const code = str.charCodeAt(i);
            // Check if the character code falls outside the alphanumeric ranges
            if (
                !(code >= '0'.charCodeAt(0) && code <= '9'.charCodeAt(0)) && // numeric (0-9)
                !(code >= 'A'.charCodeAt(0) && code <= 'Z'.charCodeAt(0)) && // upper alpha (A-Z)
                !(code >= 'a'.charCodeAt(0) && code <= 'z'.charCodeAt(0))    // lower alpha (a-z)
                ) {
                return false; // Found a non-alphanumeric character
            }
        }
        return true; // All characters were alphanumeric
    }

    isPalindrome(s) {
        if (s.length <= 1) {
            return true;
        }
        if (!this.isAlphaNumericNoRegex(s[0])) {
            return this.isPalindrome(s.slice(1));
        }
        if (!this.isAlphaNumericNoRegex(s.at(-1))) {
            return this.isPalindrome(s.slice(0, -1));
        }
        return s[0].toLowerCase() == s.at(-1).toLowerCase() && this.isPalindrome(s.slice(1, -1));
    }
}
