#include <bits/stdc++.h>
using namespace std;

class Trie{
    private:
        vector<Trie*> children;
        bool isEnd;

        Trie *searchPrefix(string prefix){
            Trie* node = this;
            for (char ch : prefix){
                ch -= 'a';
                if (node->children[ch] == nullptr){
                    return nullptr;
                }
                node = node->children[ch];
            }
            return node;
        }

    public:
        Trie() : children(26), isEnd(false){}
        
        void insert(string word){
            Trie *node = this;
            for (char ch : word){
                ch -= 'a';
                if (node->children[ch] == nullptr){
                    node->children[ch] = new Trie();
                }
                node = node->children[ch];
            }
            node->isEnd = true;
        }

        bool search(string word){
            Trie *node = this->searchPrefix(word);
            return node != nullptr && node->isEnd == true; 
        }

        bool startsWith(string prefix){
            return this->searchPrefix(prefix) != nullptr;
        }

        void remove(string word){
            Trie *node = this;
            stack<pair<Trie*, int>> nodes;
            for (char ch : word){
                ch -= 'a';
                if (node->children[ch] == nullptr){
                    return;
                }
                nodes.push({node, ch});
                node = node->children[ch];
            }
            if (!node->isEnd){
                return;
            }
            node->isEnd = false;
            while (!nodes.empty() && node->children.empty()){
                node = nodes.top().first;
                int ch = nodes.top().second;
                nodes.pop();
                delete node->children[ch];
                node->children[ch] = nullptr;
            }
        }
};
