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
