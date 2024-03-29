// tbt.h
#ifndef TBT_H
#define TBT_H

#include <iostream>

using namespace std;

struct Node{
    int val;
    Node *left, *right;
    bool rightThread, leftThread;
};

class TBT{
    private:
        Node *root;
        Node *insert(Node *root, int key);
        Node *remove(Node *root, int key);
        Node *oneChild(Node *root, Node *par, Node *ptr);
        Node *twoChild(Node *root, Node *par, Node *ptr);
        Node *noChild(Node *root, Node *par, Node *ptr);
        Node *search(Node *root, int key);
        void inorder(Node *root);
        void preorder(Node * root);
        
    public:
        TBT();
        void insert(int key);
        void remove(int key);
        void inorder();
        void preorder();
        Node *successor(Node *root);
        Node *predecessor(Node *root);
        Node *search(int key);
};
#endif
