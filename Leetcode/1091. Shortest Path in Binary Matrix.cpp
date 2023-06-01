class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0] == 1 || grid[n-1][n-1] == 1) {
            return -1;
        }

        auto heuristic = [&](int x, int y) {
            return max(abs(x - (n-1)), abs(y - (n-1)));
        };

        using Node = tuple<double, int, int, int>;
        priority_queue<Node, vector<Node>, greater<Node>> q;
        q.push({heuristic(0, 0), 0, 0, 1});

        grid[0][0] = 1;

        while (!q.empty()) {
            auto [f, i, j, d] = q.top();
            q.pop();

            if (i == n-1 && j == n-1) {
                return d;
            }

            for (auto [x, y] : vector<pair<int,int>>{{i-1,j-1},{i-1,j},{i-1,j+1},{i,j-1},{i,j+1},{i+1,j-1},{i+1,j},{i+1,j+1}}) {
                if (0 <= x && x < n && 0 <= y && y < n && !grid[x][y]) {
                    grid[x][y] = 1;
                    double g = d + 1;
                    double h = heuristic(x, y);
                    q.push({g + h, x, y, g});
                }
            }
        }

        return -1;
    }
};
