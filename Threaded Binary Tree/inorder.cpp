// inorder.cpp

#include "tbt.h"

void TBT :: inorder(Node *root){
    Node *ptr;
    if (!root){
        cout << "Tree is empty\n";
        return;
    }
    ptr = root;
    while (!ptr->leftThread){
        ptr = ptr->left;
    }
    while (ptr){
        cout << ptr->val << " ";
        ptr = successor(ptr);
    }
}

void TBT :: inorder() {
    inorder(root);
}
