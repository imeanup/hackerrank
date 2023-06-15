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
    bool isCousins(TreeNode* root, int x, int y) {
        queue<pair<TreeNode*, TreeNode*>> q;
        if (!root) return false;

        q.push(make_pair(root, nullptr));
        while (!q.empty()) {
            int n = q.size();
            TreeNode *xParent = nullptr, *yParent = nullptr;
            for (int i = 0; i < n; i++) {
                TreeNode* tmp = q.front().first;
                TreeNode* parent = q.front().second;
                q.pop();

                if (tmp->val == x) xParent = parent;
                if (tmp->val == y) yParent = parent;

                if (tmp->left) q.push(make_pair(tmp->left, tmp));
                if (tmp->right) q.push(make_pair(tmp->right, tmp));
            }
            if (xParent && yParent) return xParent != yParent;
            if ((xParent && !yParent) || (!xParent && yParent)) return false;
        }
        return false;
    }
};
