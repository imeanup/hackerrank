// predecessor.cpp

#include "tbt.h"

Node *TBT :: predecessor (Node *root){
    if (root->leftThread){
        return root->left;
    }
    else {
        root = root->left;
        while (!root->rightThread){
            root = root->right;
        }
        return root;
    }
}

void TBT :: predecessor (){
    root = predecessor(root);
}