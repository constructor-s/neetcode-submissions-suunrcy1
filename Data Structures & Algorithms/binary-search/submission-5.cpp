class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;
        while (l < r) {
            int m = l + (r - l + 1) / 2;
            if (nums[m] <= target) {
                l = m;
            } else {
                r = m - 1;
            }
        }
        return nums[l] == target ? l : -1;
    }
};
