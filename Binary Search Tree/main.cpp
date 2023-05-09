// TODO

// main.cpp
#include <iostream>
#include "bst.h"
using namespace std;

int main() {
    BST tree;
    // Tree insertion
    tree.insert(50);
    tree.insert(30);
    tree.insert(60);
    tree.insert(38);
    tree.insert(35); 
    tree.insert(55); 
    tree.insert(22); 
    tree.insert(59); 
    tree.insert(94); 
    tree.insert(13); 
    tree.insert(98); 

    cout << "Inorder Traversal: ";
    tree.inorder();
    cout << "\n";
    
    cout << "Level Order: ";
    tree.levelOrder();
    cout << "\n";
    
    cout << "Minimum key: " << tree.findMin() << "\n";
    cout << "Maximum key: " << tree.findMax() << "\n";
        
    return 0;
}
// This command need to be updated
// g++ main.cpp BST\ Deletion.cc BST\ Insertion.cc Traversal\ Inorder.cc BST.cc Level\ Order\ Traversal.cc -o main
