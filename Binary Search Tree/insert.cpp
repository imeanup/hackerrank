#include "bst.h"

Node* BST:: insert(Node *root, int key){
    Node *tmp, *par, *ptr;
    ptr = root;
    par = nullptr;
    while (ptr != nullptr){
        par = ptr;
        if (key < ptr->value){
            ptr = ptr->left;
        }
        else if (key > ptr->value){
            ptr = ptr->right;
        }
        else{
            cout << "Duplicate Key";
            return root;
        }
    }
    tmp = new Node();
    tmp->value = key;
    tmp->left = nullptr;
    tmp->right = nullptr;

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

void BST:: insert(int key) {
    root = insert(root, key);
}
