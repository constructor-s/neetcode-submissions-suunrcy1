/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        return f(root).first - 1;
    }
private:
    // Return:
    // diameterOfBinaryTree root
    // diameterOfBinaryTreeEndingAt root
    std::pair<int, int> f(TreeNode* root) {
        if (!root) return {0, 0};
        
        auto [dia_l, end_l] = f(root->left);
        auto [dia_r, end_r] = f(root->right);

        int dia = std::max(std::max(dia_l, dia_r), end_l + end_r + 1);
        int end = std::max(end_l, end_r) + 1;

        return {dia, end};
    }
};
