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
    int count = 0;

    pair<int, int> postOrder(TreeNode *node){
        if (!node) return make_pair(0, 0);
        auto [leftSum, leftCount] = postOrder(node->left);
        auto [rightSum, rightCount] = postOrder(node->right);

        int totalSum = leftSum + rightSum + node->val;
        int totalCount = leftCount + rightCount + 1;

        if (node->val == totalSum / totalCount){
            count++;
        }

        return make_pair(totalSum, totalCount);
    }
    int averageOfSubtree(TreeNode* root) {
        postOrder(root);
        return count;
    }
};

