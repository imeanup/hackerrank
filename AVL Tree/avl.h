// avl.h

#ifndef AVL_H
#define AVL_H

#include <iostream>
using namespace std;


struct Node {
    int val;
    Node *left;
    Node *right;
    int balance;
};

class AVL {
    private:
        Node *root;
        Node *insert(Node *pptr, int key);
        Node *remove(Node *pptr, int key);
        void inorder(Node *root);

    public:
        AVL();
        void insert(int key);
        void remove(int key);
        Node *insertLeftCheck(Node *pptr, bool *ptaller);
        Node *insertRightCheck(Node *pptr, bool *ptaller);
        Node *rightRotate(Node *pptr);
        Node *leftRotate(Node *pptr);
        Node *insertLeftBalance(Node *pptr);
        Node *insertRightBalance(Node *pptr);
        void inorder();
};
#endif
