// remove.cpp
#include "tbt.h"

void TBT::remove(int key) {
    root = remove(root, key);
}

Node *TBT::remove(Node *root, int key) {
    Node *par = nullptr;
    Node *ptr = root;
    int found = 0;
    while (ptr != nullptr) {
        if (key == ptr->val) {
            found = 1;
            break;
        }
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

    if (found == 0) {
        cout << key << " not present in tree\n";
    } else if (ptr->leftThread == false && ptr->rightThread == false) {
        root = twoChild(root, par, ptr);
    } else if (ptr->leftThread == false || ptr->rightThread == false) {
        root = oneChild(root, par, ptr);
    } else {
        root = noChild(root, par, ptr);
    }

    return root;
}

Node *TBT::noChild(Node *root, Node *par, Node *ptr) {
    if (par == nullptr) {
        root = nullptr;
    } else if (ptr == par->left) {
        par->leftThread = true;
        par->left = ptr->left;
    } else {
        par->rightThread = true;
        par->right = ptr->right;
    }

    delete ptr;

    return root;
}

Node *TBT::oneChild(Node *root, Node *par, Node *ptr) {
    Node *child;

    if (ptr->leftThread == false) {
        child = ptr->left;
    } else {
        child = ptr->right;
    }

    if (par == nullptr) {
        root = child;
    } else if (ptr == par->left) {
        par->left = child;
    } else {
        par->right = child;
    }

    Node *s = successor(ptr);
    Node *p = predecessor(ptr);

    if (ptr->leftThread == false) {
        p->right = s;
    } else {
        s->left = p;
    }

    delete ptr;

    return root;
}

Node *TBT::twoChild(Node *root, Node *par, Node *ptr) {
    Node *parSucc = ptr;
    Node *succ = ptr->right;

    while (succ->leftThread == false) {
        parSucc = succ;
        succ = succ->left;
    }

    ptr->val = succ->val;

    if (succ->rightThread == false) {
        root = oneChild(root, parSucc, succ);
    } else {
        root = noChild(root, parSucc, succ);
    }

    return root;
}



/*
// remove.cpp

#include "tbt.h"
TBT tbt;
Node *noChild(Node *root, Node *par, Node *ptr);
Node *oneChild(Node *root, Node *par, Node *ptr);
Node *twoChild(Node *root, Node *par, Node *ptr);

Node *TBT :: remove(Node *root, int key){
    Node *par = root, *ptr = nullptr;
    int found = 0;
    while (ptr){
        if (key == ptr->val){
            found = 1;
            break;
        }
        par = ptr;
        if (key < ptr->val){
            if(ptr->leftThread == false){
                ptr = ptr->left;
            }
            else
                break;
        }
        else {
            if(ptr->rightThread == false){
                ptr = ptr->right;
            }
            else
                break;
        }
    }
    if (found == 0){
        cout << key << " not present in tree\n";
    }
    else if (ptr->leftThread == false && ptr->rightThread == false){
        root = twoChild(root, par, ptr);
    }
    else if (ptr->leftThread == false || ptr->rightThread == false){
        root = oneChild(root, par, ptr);
    }
    else {
        root = noChild(root, par, ptr);
    }
    return root;
}

void TBT :: remove(int key){
    root = remove(root, key);
}

Node *noChild(Node *root, Node *par, Node *ptr) {
    // If node to be deleted is root
    if (par == nullptr) {
        root = nullptr;
    } else if (ptr == par->left) {
        // If node to be deleted is left child of its parent
        par->leftThread = true;
        par->left = ptr->left;
    } else {
        // If node to be deleted is right child of its parent
        par->rightThread = true;
        par->right = ptr->right;
    }
    // Delete the node
    delete ptr;
    return root;
}

// This function takes as arguments a Node pointer to the root of the tree, a Node pointer to the parent of the node to be deleted, and a Node pointer to the node to be deleted. The function returns a Node pointer to the root of the tree after the node has been deleted.

// The function first checks if the node to be deleted is the root of the tree. If it is, it sets the root to nullptr. If the node to be deleted is not the root, it checks if it is the left or right child of its parent. If it is the left child, it sets the parent’s left thread to true and sets its left child to the left child of the node to be deleted. If it is the right child, it sets the parent’s right thread to true and sets its right child to the right child of the node to be deleted. Finally, it deletes the node.


Node *oneChild(Node *root, Node *par, Node *ptr) {
    Node *child;
    // Find child of node to be deleted
    if (ptr->leftThread == false) {
        child = ptr->left;
    } else {
        child = ptr->right;
    }
    // If node to be deleted is root
    if (par == nullptr) {
        root = child;
    } else if (ptr == par->left) {
        // If node to be deleted is left child of its parent
        par->left = child;
    } else {
        // If node to be deleted is right child of its parent
        par->right = child;
    }
    // Find successor and predecessor
    Node *s = tbt.successor(ptr);
    Node *p = tbt.predecessor(ptr);
    // If ptr has left subtree
    if (ptr->leftThread == false) {
        p->right = s;
    } else {
        // If ptr has right subtree
        s->left = p;
    }
    // Delete the node
    delete ptr;
    return root;
}


// This function takes as arguments a Node pointer to the root of the tree, a Node pointer to the parent of the node to be deleted, and a Node pointer to the node to be deleted. The function returns a Node pointer to the root of the tree after the node has been deleted.

// The function first finds the child of the node to be deleted by checking if it has a left thread or not. If it does not have a left thread, its left child is its child. Otherwise, its right child is its child. The function then checks if the node to be deleted is the root of the tree. If it is, it sets the root to the child of the node to be deleted. If the node to be deleted is not the root, it checks if it is the left or right child of its parent. If it is the left child, it sets the parent’s left child to the child of the node to be deleted. If it is the right child, it sets the parent’s right child to the child of the node to be deleted.

// The function then finds the inorder successor and predecessor of the node to be deleted using the successor and predecessor functions. If the node to be deleted has a left subtree, it sets the right child of its inorder predecessor to its inorder successor. Otherwise, if it has a right subtree, it sets the left child of its inorder successor to its inorder predecessor. Finally, it deletes the node.


Node *twoChild(Node *root, Node *par, Node *ptr) {
    // Find inorder successor and its parent
    Node *parSucc = ptr;
    Node *succ = ptr->right;
    while (succ->leftThread == false) {
        parSucc = succ;
        succ = succ->left;
    }
    // Copy value of inorder successor to node to be deleted
    ptr->val = succ->val;
    // If inorder successor has right subtree
    if (succ->rightThread == false) {
        root = oneChild(root, parSucc, succ);
    } else {
        root = noChild(root, parSucc, succ);
    }
    return root;
}

// This function takes as arguments a Node pointer to the root of the tree, a Node pointer to the parent of the node to be deleted, and a Node pointer to the node to be deleted. The function returns a Node pointer to the root of the tree after the node has been deleted.

// The function first finds the inorder successor of the node to be deleted and its parent by moving to the right child of the node to be deleted and then repeatedly moving to the left child until it finds a left thread. It then copies the value of the inorder successor to the node to be deleted. If the inorder successor has a right subtree, it calls the oneChild function to remove it. Otherwise, it calls the noChild function to remove it.
*/
