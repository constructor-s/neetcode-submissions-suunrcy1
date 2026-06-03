class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        return largestArea(std::span<int>{heights});
    }

private:
    int largestArea(std::span<int> heights) {
        if (heights.empty()) return 0;
        // Find the index of the minimum which is the limiting step
        auto minIt = std::min_element(heights.begin(), heights.end());
        auto minIdx = minIt - heights.begin();
        int area = *minIt * static_cast<int>(heights.size());
        int left = largestArea(heights.subspan(0, minIdx));
        int right = largestArea(heights.subspan(minIdx + 1));
        return std::max({area, left, right});
    }
};