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

    cout << "Inorder: ";
    tree.inorder();
    cout << "\n";

    cout << "Postorder: ";
    tree.postorder();
    cout << endl;

    cout << "Preorder: ";
    tree.preorder();
    cout << endl;

    cout << "Levelorder: \n";
    tree.levelorder();
    cout << endl;

    cout << "Delete node 50\n";
    tree.remove(50);

    cout << "Inorder: ";
    tree.inorder();
    cout << endl;

    cout << "Maximum: " << tree.findMax() << endl;
    cout << "Minimum: " << tree.findMin() << endl;

    cout << "Is key 60 present: ";
    if (tree.search(60)){
        cout << "Yes\n";
    }
    else{
        cout << "No\n";
    }
    
    return 0;
}

// g++ main.cpp maximum.cpp minimum.cpp postorder.cpp preorder.cpp search.cpp remove.cpp insert.cpp inorder.cpp bst.cpp levelorder.cpp -o main
// ./main
