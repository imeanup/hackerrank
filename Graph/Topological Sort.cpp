// Kahns Algorithms aka topological sort

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class TopologicalSort {
    vector<vector<int>> adj;
    int n;

    public:
        TopologicalSort(int n) : n (n){
            adj.resize(n);
        } 
        void addEdge(int u, int v){
            adj[u].push_back(v);
        }
        void sort(){
            vector<int> in_degree(n, 0);
            for (int u = 0; u < n; u++){
                for (auto v : adj[u]){
                    in_degree[v]++;
                }
            }
            queue<int> q;
            for (int i = 0; i < n; i++){
                if (in_degree[i] == 0){
                    q.push(i);
                }
            }
            int cnt = 0;
            vector<int> top_order;
            while (!q.empty()){
                int u = q.front();
                q.pop();
                top_order.push_back(u);
                for (auto v : adj[u]){
                    if (--in_degree[v] == 0){
                        q.push(v);
                    }
                }
                cnt++;
            }
            if (cnt != n){
                cout << "There exists a cycle in the graph\n";
                return;
            }
            for (int i = 0; i < top_order.size(); i++){
                cout << top_order[i] << " ";
            }
            cout << endl; 
    }
};

int main(){
    int n = 6;
    TopologicalSort ts(n);
    vector<pair<int, int>> graph = {{5, 2}, {5, 0}, {4, 0}, {4, 1}, {2, 3}, {3, 1}};
    for (auto edge : graph){
        ts.addEdge(edge.first, edge.second);
    }
    ts.sort();
    return 0;
}

/*
// Compling info:
gpp Topological\ Sort.cpp
./Topological\ Sort      
4 5 2 0 3 1 

*/
