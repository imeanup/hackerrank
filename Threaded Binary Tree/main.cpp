// https://adtinfo.org/libavl.html/index.html
#include <iostream>
#include "tbt.h"
using namespace std;

int main(){
    TBT tree;

    tree.insert(5);
    tree.insert(10);
    tree.insert(14);
    tree.insert(16);
    tree.insert(17);
    tree.insert(20);
    tree.insert(30);
    tree.insert(13);
    tree.insert(22);

    cout << "Inorder: ";
    tree.inorder();
    cout << endl;

    cout << "Preorder: "; 
    tree.preorder();
    cout << endl;

    tree.remove(14);
    
    cout << "Inorder: ";
    tree.inorder();
    cout << endl;

    tree.remove(20);

    cout << "Inorder: ";
    tree.inorder();
    cout << endl;

    
    return 0;
}
