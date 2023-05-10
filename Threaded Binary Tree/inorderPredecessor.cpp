// predecessor.cpp

#include "tbt.h"

Node *TBT :: predecessor (Node *root){
    if (root->leftThread){
        return root->left;
    }
    else{
        root = root->left;
        
    }
}

void TBT :: predecessor (){
    root = predecessor(root);
}