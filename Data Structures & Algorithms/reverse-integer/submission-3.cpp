class Solution {
public:
    int reverse(int x) {
        if (x == INT_MIN) {
            return 0; 
        }
        if (x < 0) return -reverse(-x);
        int res = 0;
        while (x) {
            if (res > INT_MAX / 10) return 0;
            res = res * 10 + x % 10;
            std::cout << res << std::endl;
            x = x / 10;
        }
        return res;
    }
};
