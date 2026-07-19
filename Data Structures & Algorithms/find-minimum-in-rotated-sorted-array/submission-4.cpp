class Solution {
public:
    int findMin(vector<int> &nums) {
        int l = 0;
        int r = nums.size() - 1;
        while (l < r) {
            int m = l + (r - l + 1) / 2;
            if (nums[l] <= nums[m]) {
                l = m;
            } else {
                r = m - 1;
            }
        }
        return nums[(l + 1) % nums.size()];
    }
};
