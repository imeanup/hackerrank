// successor.cpp
#include "tbt.h"

Node *TBT :: successor(Node *root){
    if (root->rightThread){
        return root->right;
    }
    else{
        root = root->right;
        while (!root->leftThread){
            root = root->left;
        }
        return root;
    }
}

void TBT :: successor(){
    root = successor(root);
}
