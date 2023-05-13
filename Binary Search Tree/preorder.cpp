#include "bst.h"
#include <stack>

void BST :: preorder(Node *root){
    stack<Node*> s;
    Node *ptr = root;
    if (!ptr){
        cout << "Tree is empty\n";
        return;
    }
    s.push(ptr);
    while (!s.empty()){
        ptr = s.top();
        s.pop();
        cout << " " << ptr->value;
        if (ptr->right != nullptr){
            s.push(ptr->right);
        }
        if(ptr->left != nullptr){
            s.push(ptr->left);
        }
    }
    cout << endl;
}

void BST :: preorder(){
  preorder(root);
}
