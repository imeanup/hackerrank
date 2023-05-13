#include "bst.h"

void BST:: insert(int key) {
    root = insert(root, key);
}

Node* BST:: insert(Node *root, int key){
    Node *tmp = new Node;
    tmp->value = key;
    tmp->left = nullptr;
    tmp->right = nullptr;

    Node *ptr = root;
    Node *par = nullptr;

    while (ptr != nullptr){
        par = ptr;
        if (key < ptr->value){
            ptr = ptr->left;
        }
        else if (key > ptr->value){
            ptr = ptr->right;
        }
        else{
            cout << "Duplicate Key: " << key << endl;
            return root;
        }
    }
    
    if (!par){
        root = tmp;
    }
    else if(key < par->value){
        par->left = tmp;
    }
    else{
        par->right = tmp;
    }
    return root;
}

/*
Node* BST:: insert(Node *root, int key){
    Node *tmp = new Node;
    tmp->value = key;
    tmp->left = nullptr;
    tmp->right = nullptr;

    if (!root){
        root = tmp;
        return root;
    }
    Node *ptr = root;
 
    while (true){
        if (key < ptr->value){
            if (ptr->left == nullptr){
                ptr->left = tmp;
                break;
            }
            else {
                ptr = ptr->left;
            }   
        }
        else if (key > ptr->value){
            if (ptr->right == nullptr){
                ptr->right = tmp;
                break;
            }
            else {
                ptr = ptr->right;
            }
        }
        else{
            cout << "Duplicate Key: " << key << endl;
            break;
        }
    }
    return root;
}
*/
