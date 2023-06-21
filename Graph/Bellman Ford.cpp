#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Graph {
    public:
        unordered_map<int, vector<pair<int, int>>> graph;

        void addEdge(int u, int v, int w){
            graph[u].push_back({v, w});
        }

        void printGraph(){
            for (auto &[node, neighbors] : graph){
                cout << node << ": ";
                for (auto& [neighbor, weight] : neighbors) {
                    cout << "(" << neighbor << ", " << weight << ") ";
                }
                cout << endl;
            }
        }

        void bellmanFord(int src) {
            int V = graph.size();
            vector<int> dist(V, INT_MAX);
            vector<int> pred(V, -1);
            vector<bool> visited(V, false);

            dist[src] = 0;
            
            for (int i = 1; i <= V - 1; i++) {
				for (auto& [u, neighbors] : graph) {
					for (auto& [v, w] : neighbors) {
						if (dist[u] != INT_MAX && dist[u] + w < dist[v]) {
							dist[v] = dist[u] + w;
							pred[v] = u;
						}
					}
				}
			}

			for (auto& [u, neighbors] : graph) {
				for (auto& [v, w] : neighbors) {
					if (dist[u] != INT_MAX && dist[u] + w < dist[v]) {
						cout << "Graph contains a negative-weight cycle" << endl;
						return;
					}
				}
			}
            for (int v = 0; v < V; ++v){
                cout << src << "->" << v << " : " << dist[v] << endl;
                if (src != v){
                    printPath(pred, v);
                    cout << endl;
                }
            }
        }

    private:
        void printPath(vector<int>& pred, int v){
            if(pred[v] == -1) return;
            printPath(pred, pred[v]);
            cout << v << " ";
        }
};


int main(){
    Graph g;
    vector<tuple<int, int, int>> edges = {
        {0, 1, 8}, {0, 2, 9}, {0, 4, 7}, {1, 5, 9}, {2, 0, 5},
        {2, 3, 3}, {2, 1, -4}, {3, 2, 6}, {3, 1, 3}, {3, 5, 4}, 
        {4, 7, 16}, {5, 0, 4},{5, 6,-8}, {5, 7 ,5}, {6 ,3 ,5}, {6 ,7 ,2}
    };

    for (auto &[u, v, w] : edges){
        g.addEdge(u,v,w);
    }

    g.bellmanFord(0);

    return 0;
}
