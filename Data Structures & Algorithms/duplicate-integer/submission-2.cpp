class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> s(nums.begin(), nums.end());
        return s.size() != nums.size();
    }
};