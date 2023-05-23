// remove.cpp

// remove.cpp

#include "avl.h"

Node *AVL :: remove(Node *pptr, int key){
    Node *tmp, *succ;
    static bool shorter;
    if(pptr == nullptr){
        cout << "Key not present\n";
        shorter = false;
        return pptr;
    }
    if (key < pptr->val){
        pptr->left = remove(pptr->left, key);
        if (shorter == true){
            pptr = deleteLeftCheck(pptr, &shorter);
        }
    }
    else if (key > pptr->val){
        pptr->right = remove(pptr->right, key);
        if (shorter == true){
            pptr = deleteRightCheck(pptr, &shorter);
        }
    }
    else{
        if (pptr->left != nullptr && pptr->right != nullptr){
            succ = pptr->right;
            while (succ->left){
                succ = succ->left;
            }
            pptr->val = succ->val;
            pptr->right = remove(pptr->right, succ->val);
            if (shorter == true){
                pptr = deleteRightCheck(pptr, &shorter);
            }
        }
        else{
            tmp = pptr;
            if (pptr->left != nullptr){
                pptr = pptr->left;
            }
            else if(pptr->right != nullptr){
                pptr = pptr->right;
            }
            else{
                pptr = nullptr;
            }
            delete tmp;
            shorter = true;
        }
    }
    return pptr;
}

Node *AVL :: deleteLeftCheck(Node *pptr, bool *pshorter){
    switch(pptr->balance){
        case 0:
            pptr->balance = -1;
            *pshorter = false;
            break;
        case 1:
            pptr->balance = 0;
            break;
        case -1:
            pptr = deleteRightBalance(pptr, pshorter);
    }
 return pptr;
}

Node *AVL :: deleteRightBalance(Node *pptr, bool *pshorter){
    Node *aptr, *bptr;
    aptr = pptr->right;
    if (aptr->balance == 0){
        pptr->balance = -1;
        aptr->balance = 1;
        *pshorter = false;
        pptr = leftRotate(pptr);
    }
    else if (aptr->balance == -1){
        pptr->balance = 0;
        aptr->balance = 0;
        pptr = leftRotate(pptr);
    }
    else{
        bptr = aptr->left;
        switch(bptr->balance){
            case 0:
                pptr->balance = 0;
                aptr->balance = 0;
                break;
            case 1:
                pptr->balance = 0;
                aptr->balance = -1;
                break;
            case -1:
                pptr->balance = 1;
                aptr->balance = 0;
        }
        bptr->balance = 0;
        pptr->right = rightRotate(aptr);
        pptr = leftRotate(pptr);
    }
    return pptr;
}

Node *AVL :: deleteRightCheck(Node *pptr, bool *pshorter){
    switch(pptr->balance){
        case 0:
            pptr->balance = 1;
            *pshorter = false;
            break;
        case -1:
            pptr->balance = 0;
            break;
        case 1:
            pptr = deleteLeftBalance(pptr, pshorter);
    }
 return pptr;
}

Node *AVL :: deleteLeftBalance(Node *pptr, bool *pshorter){
    Node *aptr, *bptr;
    aptr = pptr->right;
    if (aptr->balance == 0){
        pptr->balance = 1;
        aptr->balance = -1;
        *pshorter = false;
        pptr = rightRotate(pptr);
    }
    else if (aptr->balance == -1){
        pptr->balance = 0;
        aptr->balance = 0;
        pptr = rightRotate(pptr);
    }
    else{
        bptr = aptr->right;
        switch(bptr->balance){
            case 0:
                pptr->balance = 0;
                aptr->balance = 0;
                break;
            case 1:
                pptr->balance = -1;
                aptr->balance = 0;
                break;
            case -1:
                pptr->balance = 0;
                aptr->balance = 1;
        }
        bptr->balance = 0;
        pptr->left = leftRotate(aptr);
        pptr = rightRotate(pptr);
    }
    return pptr;
}

void AVL :: remove(int key){
    root = remove(root, key);
}
