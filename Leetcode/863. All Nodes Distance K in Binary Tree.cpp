/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    unordered_map<int, vector<int>> graph;

    void createGraph(TreeNode *node, TreeNode* parent, unordered_map<int, vector<int>> &graph){
        if (node && parent){
            graph[node->val].push_back(parent->val);
            graph[parent->val].push_back(node->val);
        }
        if (node->left){
            createGraph(node->left, node, graph);
        }
        if (node->right){
            createGraph(node->right, node, graph);
        }
    }

    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        createGraph(root, nullptr, graph);
        vector<int> res;
        queue<pair<int, int>> q;
        q.push({target->val, 0});
        set<int> visited;
        visited.insert(target->val);
        while (!q.empty()){
            int temp, dist;
            tie(temp, dist) = q.front();
            q.pop();
            if (dist == k){
                res.push_back(temp);
                continue;
            }
            for (auto nbr: graph[temp]){
                if (visited.find(nbr) == visited.end()){
                    visited.insert(nbr);
                    q.push({nbr, dist+1});
                }
            }
        }
        return res;
    }
};
