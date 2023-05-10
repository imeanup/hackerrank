class Solution {
public:
    TreeNode* increasingBST(TreeNode* root) {
        // Create a new dummy node to serve as the root of the modified tree
        TreeNode* dummy = new TreeNode(0);
        // Create a pointer to the current node in the modified tree
        TreeNode* cur = dummy;
        
        // Traverse the tree in-order and modify each node
        stack<TreeNode*> s;
        TreeNode* node = root;
        while (node || !s.empty()) {
            // Traverse the left subtree
            while (node) {
                s.push(node);
                node = node->left;
            }
            
            // Visit the current node and modify it
            node = s.top();
            s.pop();
            cur->right = new TreeNode(node->val);
            cur = cur->right;
            
            // Traverse the right subtree
            node = node->right;
        }
        
        // Return the modified tree (skip the dummy node)
        return dummy->right;
    }
};

class Solution {
public:
    TreeNode* increasingBST(TreeNode* root) {
        vector<int> vals;
        inorder(root, vals);
        TreeNode* ans = new TreeNode(0);
        TreeNode* cur = ans;
        for (int v : vals) {
            cur->right = new TreeNode(v);
            cur = cur->right;
        }
        return ans->right;
    }
    
    void inorder(TreeNode* node, vector<int>& vals) {
        if (node == nullptr) return;
        inorder(node->left, vals);
        vals.push_back(node->val);
        inorder(node->right, vals);
    }
};

class Solution {
    TreeNode* cur;
public:
    TreeNode* increasingBST(TreeNode* root) {
        TreeNode* ans = new TreeNode(0);
        cur = ans;
        inorder(root);
        return ans->right;
    }
    
    void inorder(TreeNode* node) {
        if (node == nullptr) return;
        inorder(node->left);
        node->left = nullptr;
        cur->right = node;
        cur = node;
        inorder(node->right);
    }
};

