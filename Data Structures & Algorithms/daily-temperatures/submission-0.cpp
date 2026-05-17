class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res(temperatures.size(), 0);

        for (int i = temperatures.size() - 2; i >= 0; --i) {
            int j = i + 1;
            while (temperatures[i] >= temperatures[j]) {
                if (res[j] == 0) break;
                j = j + res[j];
            }
            if (temperatures[i] < temperatures[j]) res[i] = j - i;
        }

        return res;
    }
};
