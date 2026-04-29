class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        if (nums.empty()) return false;

        set<int> s;
        for (int i : nums) {
            if (s.count(i)) return true;
            s.insert(i);
        }

        return false;
    }
};