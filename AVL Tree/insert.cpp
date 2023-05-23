// insert.cpp
#include "avl.h"

Node *AVL :: insert(Node *pptr, int key){
    static bool taller;
    if (pptr == nullptr){
        pptr = new Node;
        pptr->val = key;
        pptr->left = nullptr;
        pptr->right = nullptr;
        pptr->balance = 0;
        taller = true;
    }

    else if (key < pptr->val){
        pptr->left = insert(pptr->left, key);
        if (taller == true){
            pptr = insertLeftCheck(pptr, &taller);
            }
        }
        else if (key > pptr->val){
            pptr->right = insert(pptr->right, key);
            if (taller == true){
                pptr = insertRightCheck(pptr, &taller);
            }
        }
        else{
            cout << "Duplicate Key\n";
            taller = false;
        }
    return pptr;
}

Node *AVL :: insertLeftCheck(Node *pptr, bool *ptaller){
    switch(pptr->balance){
        case 0:
            pptr->balance = 1;
            break;
        case -1:
            pptr->balance = 0;
            *ptaller = false;
            break;
        case 1:
            pptr = insertLeftBalance(pptr);
            *ptaller = false;
    }
 return pptr;
}

Node *AVL :: insertRightCheck(Node *pptr, bool *ptaller){
    switch(pptr->balance){
        case 0:
            pptr->balance = -1;
            break;
        case 1:
            pptr->balance = 0;
            *ptaller = false;
            break;
        case -1:
            pptr = insertRightBalance(pptr);
            *ptaller = false;
    }
 return pptr;
}


Node *AVL :: insertLeftBalance(Node *pptr){
    Node *aptr, *bptr;
    aptr = pptr->left;
    if (aptr->balance == 1){
        pptr->balance = 0;
        aptr->balance = 0;
        pptr = rightRotate(pptr);
    }

    else{
        bptr = aptr->right;
        switch(bptr->balance){
            case -1:
                pptr->balance = 0;
                aptr->balance = 1;
                break;
            case 1:
                pptr->balance = -1;
                aptr->balance = 0;
                break;
            case 0:
                pptr->balance = 0;
                aptr->balance = 0;
        }
        bptr->balance = 0;
        pptr->left = leftRotate(aptr);
        pptr = rightRotate(pptr);
    }
    return pptr;
}

Node *AVL :: insertRightBalance(Node *pptr){
    Node *aptr, *bptr;
    aptr = pptr->right;

    if (aptr->balance == -1){
        pptr->balance = 0;
        aptr->balance = 0;
        pptr = leftRotate(pptr);
    }
    else{
        bptr = aptr->left;
        switch(bptr->balance){
            case -1:
                pptr->balance = 1;
                aptr->balance = 0;
                break;
            case 1:
                pptr->balance = 0;
                aptr->balance = -1;
                break;
            case 0:
                pptr->balance = 0;
                aptr->balance = 0;
            }
        bptr->balance = 0;
        pptr->right = rightRotate(aptr);
        pptr = leftRotate(pptr);
    }
 return pptr;
}

void AVL :: insert(int key){
    root = insert(root, key);
}

/*

#include<bits/stdc++.h>
using namespace std;

struct Node {
    int key;
    Node *left;
    Node *right;
    int height;
};

int height(Node *N) {
    if (N == nullptr)
        return 0;
    return N->height;
}

Node* newNode(int key) {
    Node* node = new Node();
    node->key = key;
    node->left = NULL;
    node->right = NULL;
    node->height = 1;
    return(node);
}

Node *rightRotate(Node *y) {
    Node *x = y->left;
    Node *T2 = x->right;

    x->right = y;
    y->left = T2;

    y->height = max(height(y->left),
                    height(y->right)) + 1;
    x->height = max(height(x->left),
                    height(x->right)) + 1;

    return x;
}

Node *leftRotate(Node *x) {
    Node *y = x->right;
    Node *T2 = y->left;

    y->left = x;
    x->right = T2;

    x->height = max(height(x->left),
                    height(x->right)) + 1;
    y->height = max(height(y->left),
                    height(y->right)) + 1;

    return y;
}

int getBalance(Node *N) {
    if (N == NULL)
        return 0;
    return height(N->left) - height(N->right);
}

Node* insert(Node* node, int key) {
    if (node == NULL)
        return(newNode(key));

    if (key < node->key)
        node->left = insert(node->left, key);
    else if (key > node->key)
        node->right = insert(node->right, key);
    else
        return node;

    node->height = 1 + max(height(node->left),
                           height(node->right));

    int balance = getBalance(node);

    if (balance > 1 && key < node->left->key)
        return rightRotate(node);

    if (balance < -1 && key > node->right->key)
        return leftRotate(node);

    if (balance > 1 && key > node->left->key) {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }

    if (balance < -1 && key < node->right->key) {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }

    return node;
}

*/
