#include <bits/stdc++.h>
#include <atcoder/dsu>
using namespace std;
using namespace atcoder;

using ll = int64_t;
const ll MOD = 998244353;

int N, Q;
vector<vector<int>> g;
int batchSize = 2000;

vector<int> generateParent() {
    vector<int> visited(N, 0);
    vector<int> parent(N, -1);
    queue<int> q;
    for (int i = 0; i < N; i++) {
        if (visited[i]) continue;
        visited[i] = 1;
        q.push(i);
        while (!q.empty()) {
            int currNode = q.front();
            q.pop();
            for (auto &nextNode : g[currNode]) {
                if (visited[nextNode] == 0) {
                    visited[nextNode] = 1;
                    parent[nextNode] = currNode;
                    q.push(nextNode);
                }
            }
        }
    }
    return parent;
}

int main() {
    cin >> N >> Q;
    g.resize(N);
    vector<int> history = {0};
    vector<int> currentParent;
    vector<unordered_set<int>> set(N);

    dsu uf(N);
    vector<pair<int, int>> edgeMemory;

    for (int q = 0; q < Q; q++) {
        if (q % batchSize == 0) {
            currentParent = generateParent();
            for (auto &edge : edgeMemory) {
                uf.merge(edge.first, edge.second);
            }
            edgeMemory.clear();
        }

        int A, B, C;
        ll a, b, c;
        cin >> a >> b >> c;
        a *= (history.back() + 1); a %= MOD;
        b *= (history.back() + 1); b %= MOD; 
        c *= (history.back() + 1); c %= MOD; 

        A = 1 + (a % 2);
        B = 1 + (b % N);
        C = 1 + (c % N);
        B--, C--;

        if (A == 1) {
            set[B].insert(C);
            set[C].insert(B);
            g[B].push_back(C);
            g[C].push_back(B);
            edgeMemory.push_back({B, C});
        }
        else {
            vector<int> candidate;
            if (uf.same(B, C)) {
                candidate = {currentParent[B], currentParent[C]};
            }
            else {
                for (auto &edge : edgeMemory) {
                    if (edge.first == B || edge.first == C) {
                        candidate.push_back(edge.second);
                    }
                    if (edge.second == B || edge.second == C) {
                        candidate.push_back(edge.first);
                    }
                }
            }

            int output = -1;
            for (auto &can : candidate) {
                if (set[B].find(can) == set[B].end()) continue;
                if (set[C].find(can) == set[B].end()) continue;
                output = can;
            }

            output++;
            cout << output << "\n";
            history.push_back(output);
        }
    }
    return 0;
}