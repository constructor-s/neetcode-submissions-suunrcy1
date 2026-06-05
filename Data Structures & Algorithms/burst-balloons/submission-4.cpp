class Solution {
public:
    int maxCoins(vector<int>& nums) {
        std::vector<int> nums1(nums.size() + 2, 1);
        std::copy(nums.begin(), nums.end(), nums1.begin() + 1);

        std::vector<std::vector<int>> cache(nums.size() + 2, std::vector<int>(nums.size() + 2, -1));

        // for (auto it = nums1.begin(); it != nums1.end(); ++it) {
        //     std::cout << *it << ' ';
        // }
        // std::cout << '\n';

        return _maxCoins(
            1, nums.size(),
            nums1,
            cache
        );
    }
private:
    int _maxCoins(int l, int r, const vector<int> &nums, std::vector<std::vector<int>> &cache) {
        if (l > r) return 0;
        if (cache[l][r] != -1) return cache[l][r];

        int maxScore = 0;
        for (int m = l; m <= r; ++m) {
            int score = _maxCoins(l, m - 1, nums, cache) + nums[l - 1] * nums[m] * nums[r + 1] + _maxCoins(m + 1, r, nums, cache);
            if (score > maxScore) maxScore = score;
        }
        cache[l][r] = maxScore;
        // std::cout << l << ' ' << r << " => " << maxScore << '\n';
        return maxScore;
    }
};
