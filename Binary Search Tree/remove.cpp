#include "bst.h"

Node *noChild(Node *root, Node *par, Node *ptr);
Node *oneChild(Node *root, Node *par, Node *ptr);
Node *twoChild(Node *root, Node *par, Node *ptr);

Node *BST :: remove(Node *root, int key){
    Node *par, *ptr;
    ptr = root;
    par = nullptr;
    while (ptr){
        if (key == par->value){
            break;
        }
        par = ptr;
        if (key < ptr->value){
            ptr = ptr->left;
        }
        else{
            ptr = ptr->right;
        }
    }
    if (!ptr){
        cout << key << " not pesent in tree\n";
    }
    else if (ptr->left && ptr->right){
        root = twoChild(root, par, ptr);
    }
    else if (ptr->left || ptr->right){
        root = oneChild(root, par, ptr);
    }
    else{
        root = noChild(root, par, par);
    }
    return root;
}

Node *noChild(Node *root, Node *par, Node *ptr){
    if (!par){
        root = nullptr;
    }
    else if (ptr == par->left){
        par->left = nullptr;
    }
    else{
        par->right = nullptr;
    }
    free(ptr);
    return root;
}

Node *oneChild(Node *root, Node *par, Node *ptr){
    Node *child;
    if (ptr->left){
        child = ptr->left;
    }
    else{
        child = ptr->right;
    }
    if (!par){
        root = child;
    }
    else if(ptr == par->left){
        par->left = child;
    }
    else{
        par->right = child;
    }
    free(ptr);
    return root;
}

Node *twoChild(Node *root, Node *par, Node *ptr){
    Node *succ, *parsucc;
    parsucc = ptr;
    succ = ptr->right;
    while (succ->left){
        parsucc = succ;
        succ = succ->left;
    }
    ptr->value = succ->value;
    if (!succ->left && !succ->right){
        root = noChild(root, parsucc, succ);
    }
    else{
        root = oneChild(root, parsucc, succ);
    }
    return root;
}

void BST :: remove(int key){
    root = remove(root, key);
}
