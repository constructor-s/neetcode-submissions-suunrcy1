class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        return largestRectangleArea(std::span<int>{heights.data(), heights.size()});
    }

    int largestRectangleArea(const std::span<int> & heights) {
        if (heights.empty()) return 0;
        // Find the index of the minimum which is the limiting step
        auto minIt = std::min_element(heights.begin(), heights.end());
        int area = *minIt * heights.size();
        int left = largestRectangleArea(std::span<int>(heights.begin(), minIt));
        int right = largestRectangleArea(std::span<int>(minIt + 1, heights.end()));
        return max(max(area, left), right);
    }
};
