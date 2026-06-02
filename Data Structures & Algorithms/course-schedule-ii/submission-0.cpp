class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        std::vector<std::vector<int>> prereq(numCourses);
        for (const auto &item : prerequisites) {
            prereq[item[0]].push_back(item[1]);
        }
        
        std::vector<int> output; output.reserve(numCourses);
        std::vector<bool> visit(numCourses, false);
        std::vector<bool> cycle(numCourses, false);

        for (int course = 0; course < numCourses; ++course) {
            if (!dfs(course, prereq, visit, cycle, output)) return {};
        }

        return output;
    }
private:
    bool dfs(int course, 
            const std::vector<std::vector<int>> &prereq,
            std::vector<bool> &visit,
            std::vector<bool> &cycle,
            std::vector<int> &output) {
        if (visit[course]) return true; // another course already have this prereq, and already has it done

        if (cycle[course]) return false; // a course on the unfinished stack is a prereq
        cycle[course] = true;
        
        for (int pre : prereq[course]) {
            if (!dfs(pre, prereq, visit, cycle, output)) return false;
        }
        // All prereqs has been satisfied without cycle
        cycle[course] = false; // no longer a cycle
        visit[course] = true; // this course is now done
        output.push_back(course);
        return true;
    }
};
