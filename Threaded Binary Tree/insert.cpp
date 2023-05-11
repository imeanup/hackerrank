// insert.cpp

#include "tbt.h"

Node *TBT :: insert(Node *root, int key){
    Node *tmp, *par, *ptr;
    int found = 0;
    ptr = root;
    par = nullptr;
    while (ptr){
        if (key == ptr->val){
            found = 1;
            break;
        }
        par = ptr;
        if (key < ptr->val){
            if (!ptr->leftThread){
                ptr = ptr->left;
            }
            else{
                break;
            }
        }
        else{
            if (!ptr->rightThread){
                ptr = ptr->right;
            }
            else{
                break;
            }
        }
    }
    if (found){
        cout << "Duplicate Key\n";
    }
    else{
        tmp = new Node;
        // TODO
    }
}

void TBT :: insert(int key){
    root = insert(root, key);
}
