class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        auto s = std::unordered_set<int>(nums.begin(), nums.end());
        return s.size() != nums.size();
    }
};