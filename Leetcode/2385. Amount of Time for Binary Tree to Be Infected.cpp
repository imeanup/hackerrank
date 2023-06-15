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
    int amountOfTime(TreeNode* root, int start) {
        unordered_map<int, vector<int>> graph;
        dfs(root, graph);
        return bfs(start, graph);
    }

private:
    void dfs(TreeNode *node, unordered_map<int, vector<int>> &graph, TreeNode*parent = nullptr){
        if (!node) return;
        graph[node->val] = {};
        if (parent){
            graph[node->val].push_back(parent->val);
            graph[parent->val].push_back(node->val);
        }
        dfs(node->left, graph, node);
        dfs(node->right, graph, node);
    }

    int bfs(int start, unordered_map<int, vector<int>> &graph){
        int level = 0;
        queue<int> q{{start}};
        unordered_set <int>visited;
        while (!q.empty()){
            for (int i = q.size(); i > 0; --i){
                int curr = q.front();
                q.pop();
                visited.insert(curr);
                for (int nbr : graph[curr]){
                    if (!visited.count(nbr)){
                        q.push(nbr);
                    }
                }
            }
            ++level;
        }
        return level-1;
    }
};

