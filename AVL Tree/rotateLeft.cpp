// leftRotate.cpp

#include "avl.h"

Node *AVL :: leftRotate(Node *pptr){
    Node *aptr;
    aptr = pptr->right;
    pptr->right = aptr->left;
    aptr->left = pptr;
    return aptr;
}
