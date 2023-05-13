#include "bst.h"
#include <stack>

void BST :: inorder(Node *root){
    stack<Node*> s;
    Node *ptr = root;
    if (!ptr){
        cout << "Tree is empty\n";
        return;
    }
    while(true){
        while (ptr->left != nullptr){
            // cout << " " << ptr->value; // In stack
            s.push(ptr);
            ptr = ptr->left;
        }
        while (ptr->right == nullptr){
            cout << " " << ptr->value;
            if (s.empty()){
                return;
            }
            ptr = s.top();
            // cout << " " << ptr->value; // Out-of stack
            s.pop();
        }
        cout << " " << ptr->value;
        ptr = ptr->right;
    }
    cout << endl;
}

void BST::inorder() {
    inorder(root);
}
