// bst.h
#ifndef BST_H
#define BST_H

#include <iostream>
using namespace std;

struct Node {
    int value;
    Node *left;
    Node *right;
    Node(int value): value(value), left(nullptr), right(nullptr) {}
};

class BST {
private:
    Node *root;
    Node *insert(Node *root, int key);
    Node *remove(Node *root, int key);
    Node *search(Node *root, int key);
    void inorder(Node *root);
    void preorder(Node *root);
    void postorder(Node *root);
    void levelOrder(Node *root);
public:
    BST();
    void search(int key);
    void insert(int key);
    void remove(int key);
    void inorder();
    void preorder();
    void postorder();
    void levelOrder();
};

#endif
