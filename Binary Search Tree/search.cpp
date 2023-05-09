#include "bst.h"

Node *BST :: search(Node *root, int key){
  while (root){
    if (key < root->value){
      root = root->left;
    }
    else if (key > root->value){
      root = root->right;
    }
    else{
      return root;
    }
  }
  return nullptr; 
}

bool BST :: search(int key) {
    return search(root, key) != nullptr;
}
