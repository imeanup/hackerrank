// main.cpp
#include <iostream>
#include "avl.h"
using namespace std;

int main(){
    AVL tree;
    tree.insert(18);
    tree.insert(15);
    tree.insert(20);
    tree.insert(10);
    tree.insert(16);
    tree.insert(24);
    tree.insert(5);
    tree.insert(12);

    cout << "Inorder: ";
    tree.inorder();
    cout << "\n";

    tree.insert(14);
    cout << "Inorder: ";
    tree.inorder();
    cout << "\n";

    return 0;
}

// main.cpp avl.cpp inorder.cc insert.cpp leftRotation.cpp rightRotation.cpp -o output
