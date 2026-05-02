class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        std::vector<int> dp(amount + 1, amount + 1);
        for (size_t i = 0; i < amount + 1; ++i) dp[i] = -1;
        dp[0] = 0;
        for (int i = 1; i < amount + 1; ++i) {
            for (int c : coins) {
                if (i - c >= 0 && 
                dp[i - c] != -1 && 
                (dp[i] == -1 || dp[i - c] + 1 < dp[i])) {
                    dp[i] = dp[i - c] + 1;
                }
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
};
