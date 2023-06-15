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
    private:
        TreeNode *finMin(TreeNode *node){
            while (node && node->left != nullptr){
                node = node->left;
            }
            return node;
        }
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) return nullptr;
        if (key < root->val){
            root->left = deleteNode(root->left, key);
        }
        else if (key > root->val){
            root->right = deleteNode(root->right, key);
        }
        else{
            if (root->right == nullptr){
                TreeNode *tmp = root->left;
                delete root;
                return tmp;
            }
            else if (root->left == nullptr){
                TreeNode *tmp = root->right;
                delete root;
                return tmp;
            }
            else if (!root->left && !root->right){
                delete root;
                return nullptr;
            }
            else{
                TreeNode *tmp = finMin(root->right);
                root->val = tmp->val;
                root->right = deleteNode(root->right, tmp->val);
            }
        }
        return root;
    }
};


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
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) return nullptr;
        TreeNode* cur = root;
        TreeNode* parent = nullptr;
        while (cur && cur->val != key){
            parent = cur;
            if (key < cur->val) cur = cur->left;
            else cur = cur->right;
        }
        if (!cur) return root;
        if (!cur->left && !cur->right){
            if (!parent) return nullptr;
            if (parent->left == cur) parent->left = nullptr;
            else parent->right = nullptr;
            delete cur;
        }
        else if (!cur->left || !cur->right){
            TreeNode* child = cur->left ? cur->left : cur->right;
            if (!parent) return child;
            if (parent->left == cur) parent->left = child;
            else parent->right = child;
            delete cur;
        }
        else{
            TreeNode* temp = findMin(cur->right);
            int minVal = temp->val;
            deleteNode(root, minVal);
            cur->val = minVal;
        }
        return root;
    }

private:
    TreeNode* findMin(TreeNode* node){
        while (node && node->left){
            node = node->left;
        }
        return node;
    }
};
