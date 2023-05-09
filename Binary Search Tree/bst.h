// bst.h
#ifndef BST_H
#define BST_H

#include <iostream>
using namespace std;

struct Node {
    int value;
    Node *left;
    Node *right;
};

class BST {
private:
    Node *root;
    Node* insert(Node *root, int key);
    Node *deletion(Node *root, int key);
    void inorder(Node *root);
    void levelOrder(Node *root);
public:
    BST();
    void insert(int key);
    void deletion(int key);
    void inorder();
    void levelOrder();
};

#endif
