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

        std::ranges::sort(intervals, {}, &Interval::start);
        
        // Searches the range [first, last) for two consecutive "true" elements. 
        // An iterator to the first of the first pair of "true" elements, that is, 
        // the first iterator it such that p(*it, *(it + 1)) != false. 
        // If no such elements are found, last is returned. 
        auto it = std::adjacent_find(intervals.begin(), intervals.end(),[](const auto& a, const auto& b){
            return a.end > b.start;
        });
        return it == intervals.end();
    }
};
