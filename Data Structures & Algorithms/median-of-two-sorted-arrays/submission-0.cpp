class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        return f(nums1, nums2);
    }

    double f(std::span<int> nums1, std::span<int> nums2) {
        if (nums1.size() + nums2.size() == 1) {
            return nums1.size() ? nums1[0] : nums2[0];
        }
        if (nums1.size() + nums2.size() == 2) {
            if (nums1.size() == 0) {
                return 0.5 * (nums2[0] + nums2[1]);
            } else if (nums2.size() == 0) {
                return 0.5 * (nums1[0] + nums1[1]);
            } else {
                return 0.5 * (nums1[0] + nums2[0]);
            }
        }
        
        if (nums1.size() == 0) {
            nums2 = nums2.subspan(1);
        } else if (nums2.size() == 0) {
            nums1 = nums1.subspan(1);
        } else if (nums1[0] < nums2[0]) {
            nums1 = nums1.subspan(1);
        } else {
            nums2 = nums2.subspan(1);
        }

        if (nums1.size() == 0) {
            nums2 = nums2.subspan(0, nums2.size() - 1);
        } else if (nums2.size() == 0) {
            nums1 = nums1.subspan(0, nums1.size() - 1);
        } else if (nums1[nums1.size() - 1] > nums2[nums2.size() - 1]) {
            nums1 = nums1.subspan(0, nums1.size() - 1);
        } else {
            nums2 = nums2.subspan(0, nums2.size() - 1);
        }

        return f(nums1, nums2);
    }
};
