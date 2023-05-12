// insert.cpp
#include "tbt.h"

void TBT::insert(int key) {
    root = insert(root, key);
}

Node *TBT::insert(Node *root, int key) {
    // Create a new node
    Node *tmp = new Node;
    tmp->val = key;
    tmp->leftThread = true;
    tmp->rightThread = true;

    // If tree is empty
    if (root == nullptr) {
        root = tmp;
        return root;
    }

    // Find parent of new node
    Node *par = nullptr;
    Node *ptr = root;
    while (ptr != nullptr) {
        par = ptr;
        if (key < ptr->val) {
            if (ptr->leftThread == false) {
                ptr = ptr->left;
            } else {
                break;
            }
        } else {
            if (ptr->rightThread == false) {
                ptr = ptr->right;
            } else {
                break;
            }
        }
    }

    // Insert new node as left or right child of parent
    if (key < par->val) {
        tmp->left = par->left;
        tmp->right = par;
        par->leftThread = false;
        par->left = tmp;
    } else {
        tmp->left = par;
        tmp->right = par->right;
        par->rightThread = false;
        par->right = tmp;
    }

    return root;
}

/*

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
        tmp->val = key;
        tmp->leftThread = true;
        tmp->rightThread = true;

        if (!par){
            root = tmp;
            tmp->left = nullptr;
            tmp->right = nullptr;
        }
        else if (key < par->val){
            tmp->left = par->left;
            tmp->right = par;
            par->leftThread = false;
            par->left = tmp;
        }
        else {
            tmp->left = par;
            tmp->right = par->right;
            par->rightThread = false;
            par->right = tmp;
        }
    }
    return root;
}
*/
