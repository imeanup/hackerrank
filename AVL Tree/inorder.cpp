// inorder.cpp

#include "avl.h"

void AVL :: inorder(Node *root){
    if (root) {
        inorder(root->left);
        cout << root->val << " ";
        inorder(root->right);
    }
}

void AVL::inorder() {
    inorder(root);
}
