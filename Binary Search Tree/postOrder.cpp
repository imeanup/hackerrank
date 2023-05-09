#include "bst.h>
#include <stack>

void BST :: postorder(Node *root){
    stack <Node*> s;
    Node *q, *ptr = root;
    if (!ptr){
        cout << "Tree is empty\n";
        return;
    }
    q = root;
    while (true){
        while (ptr->left != nullptr){
            // cout << ptr->value << " ";
            s.push(ptr);
            ptr = ptr->left;
        }
        while (ptr->right == nullptr || ptr->right == q){
            cout << ptr->value << " ";
            q = ptr;
            // cout << q->value << " ";
            if (s.empty()){
                return;
            }
            ptr = s.top();
            // cout << ptr->value << " ";
            s.pop();
        }
        // cout << ptr->value << " ";
        s.push(ptr);
        ptr = ptr->right;
    }
    cout << endl;
}

void BST :: postorder(){
  postorder(root);
}
