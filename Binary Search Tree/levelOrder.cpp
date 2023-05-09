#include "BST.h"
#include <queue>

void BST :: levelOrder(Node *root){
    if (!root){
        return;
    }
    queue<Node*> q;
    q.push(root);
    int level = 0;
    while (!q.empty()){
        int level_size = q.size();
        cout << "Level: " << level << " -> " ;
        for (int i = 0; i < level_size; i++){
            Node *tmp = q.front();
            q.pop();
            
            cout << tmp->value << " ";
            if (tmp->left){
                q.push(tmp->left);
            }
            if (tmp->right){
                q.push(tmp->right);
            }
        }  
        cout << endl;
        level++;
    }
}

void BST :: levelOrder(){
    levelOrder(root);
}
