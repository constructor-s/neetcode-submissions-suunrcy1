class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) : k(k) {
        for (int n : nums) {
            this->add(n);
        }
    }
    
    int add(int val) {
        if (pq.size() < k) {
            pq.push(val);  
        } else if (val > pq.top()) {
            pq.pop();
            pq.push(val);
        }
        return pq.top();
    }
private:
    int k;
    std::priority_queue<int, vector<int>, std::greater<int>> pq;
};
