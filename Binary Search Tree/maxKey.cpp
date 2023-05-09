#include "bst.h"

int BST :: findMax() {
    if (!root){
      cout << "Tree is empty\n";
    }
    Node *current = root;
    while (current->right != nullptr) {
        current = current->right;
    }
    return current->value;
}
