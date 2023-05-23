// rightRotate.cpp

#include "avl.h"

Node *AVL :: rightRotate(Node *pptr){
    Node *aptr;
    aptr = pptr->left;
    pptr->left = aptr->right;
    aptr->right = pptr;
    return aptr;
}
