class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        std::vector<std::vector<std::string>> res;

        // Each row can only have one queen
        // Others need to be marked more explicitly
        std::set<int> cols;
        std::set<int> diag1; // x + y == constant
        std::set<int> diag2; // x - y == constant

        std::vector<std::string> board(n, std::string(n, '.'));

        backtrack(0, res, n, board, cols, diag1, diag2);

        return res;
    }
private:
    void backtrack(const int i, std::vector<std::vector<std::string>> & res, 
                    int n, std::vector<std::string> & board,  
                    std::set<int> & cols, std::set<int> & diag1, std::set<int> & diag2) {
        if (i == n) {
            res.push_back(board);
            return;
        }

        for (int j = 0; j < n; ++j) {
            // std::cout << i << ", " << j << '\n';
            // std::cout << (diag1.find(i + j) == cols.end()) << '\n';
            if ((cols.find(j) == cols.end()) && 
                (diag1.find(i + j) == diag1.end()) &&
                (diag2.find(i - j) == diag2.end())) {
                cols.insert(j);
                diag1.insert(i + j);
                diag2.insert(i - j);

                board[i][j] = 'Q';
                backtrack(i + 1, res, n, board, cols, diag1, diag2);
                board[i][j] = '.';

                diag2.erase(i - j);
                diag1.erase(i + j);
                cols.erase(j);
            }
        }
    }
};
