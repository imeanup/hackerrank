// search.cpp

#include "tbt.h"

Node *TBT :: search(int key){
    return search(root, key);
}

Node *TBT :: search(Node* root, int key){
    while (root){
        if (key < root->val){
            root = root->left;
        }
        else if (key > root->val){
            root = root->right;
        }
        else{
            return root;
        }
    }
    return nullptr;
}
