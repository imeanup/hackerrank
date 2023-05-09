#include "bst.h"

int BST :: findMin() {
    if (!root){
      cout << "Tree is empty\n";
    }
    Node *current = root;
    while (current->left != nullptr) {
        current = current->left;
    }
    return current->value;
}
