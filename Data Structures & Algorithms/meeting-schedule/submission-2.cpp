/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        if (intervals.size() <= 1) return true;

        std::sort(intervals.begin(), intervals.end(), [](const auto& a, const auto& b){
            return a.start < b.start;
        });
        for (size_t i = 1; i < intervals.size(); ++i) {
            if (intervals[i-1].end > intervals[i].start) return false;
        }
        return true;
    }
};
