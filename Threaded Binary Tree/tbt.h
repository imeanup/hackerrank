// tbt.h
#ifndef TBT_H
#define TBT_H

#include <iostream>

using namespace std;

struct Node{
    int val;
    Node *left, *right;
    bool rightThread, leftThread;
};
#endif