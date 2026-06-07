class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        this->h.reserve(k + 1);
        for (int n : nums) {
            this->add(n);
        }
        for (int n : h) {
            std::cout << n << " ";
        }
        std::cout << "\n";
    }
    
    int add(int val) {
        // C++ implements max heap
        // The heap will track the opposite number
        val = -val;
        if (h.size() < k) {
            h.push_back(val);
            std::push_heap(h.begin(), h.end());
        } else if (val < h[0]) {
            h.push_back(val);
            std::push_heap(h.begin(), h.end());
            std::pop_heap(h.begin(), h.end());
            h.pop_back();
        }
        return -h[0];
    }
private:
    int k;
    std::vector<int> h;
};
