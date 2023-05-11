// preorder.cpp

#include "tbt.h"

void TBT :: preorder(Node *root){
    Node *ptr;
    if (!root){
        cout << "Tree is empty\n";
        return;
    }
    ptr = root;
    while (ptr){
        cout << ptr->val << " ";
        if (!ptr->leftThread){
            ptr = ptr->left;
        }
        else if (!ptr->rightThread){
            ptr = ptr->right;
        }
        else{
            while (ptr && ptr->rightThread){
                ptr = ptr->right;
            }
            if (ptr){
                ptr = ptr->right;
            }
        }
    }
}

void TBT :: preorder(){
    preorder(root);
}
