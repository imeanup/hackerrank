<!-- # D - Grid and Magnet

まず、磁石が置かれていないマス $S$ について、その自由度を求める方法について考えます。
これは、例えばグリッドグラフ上の深さ優先探索で求めることができます。
磁石が置かれていない各マスを頂点とし（以下マス $A$ に対応する頂点を頂点 $A$ とよぶことにします）、そしてマス $A$ からマス $B$ に $1$ 回の移動で行けるとき、かつそのときに限り頂点 $A$ から頂点 $B$ に辺が伸びているようなグラフを考えます。このときに頂点 $S$ から辺を辿って到達できる頂点は深さ優先探索で列挙でき、その数を数えることができます。（幅優先探索でも問題ありません。）これをすべての（磁石の置かれていない）マスについて行うことで答えを得ることができます。

しかし、ここで、このグラフは頂点・辺ともに最大で $O(H W)$ 個(本) 存在するため、$1$ マスの自由度を求めるのに $O(H W)$ の計算量がかかり、全体で最悪 $O(H^2 W^2)$ の計算量がかかってしまい、時間制限に間に合わせるのは厳しいです。

そこで、マス $A$ から マス $B$ へ移動でき、マス $B$ に隣接したマスに磁石が置かれていない時、マス $A$ とマス $B$ の自由度は等しいということに注目します。 なぜなら、マス $B$ に隣接したマスに磁石が置かれていないとき、マス $A$ からマス $B$ へ移動する経路を逆になぞることによってマス $B$ からマス $A$ に到達でき、このとき、任意の他のマス $C$ について、「マス $A$ からマス $C$ に到達できる」ことと「マス $B$ からマス $C$ に到達できる」ことが同値になるからです。これにより、あるマス $S$ から到達できるマスを探索している間に途中で到達したマス $S'$ について マス $S'$ が磁石に隣接していない場合、マス $S'$ から始めて到達できるマスの数を再度調べる必要はないことが分かります。これはすでに一度以上そのマスが探索されたかのフラグを持っておくことで管理することができます。

このようにしたときの計算量について考えます。各頂点から伸びている辺の数は定数なので基本的には探索において登場した（移動を開始したマス, そこから到達できたマス）のペアの数に比例した時間量がかかります。

後者に注目して、各マスが何回「そこから到達できたマス」として登場するかについて考えます。磁石と隣接していないマス $T$ については、ちょうど $1$ 回登場します。なぜなら、$T$ に $2$ 回以上訪れたとすると、ある $2$ つの異なるマス $S, S'$ から $T$ に到達するような探索を行なっていますが、ことのき $S$ から $T$ を経由して $S'$ に到達できる（同様に $S'$ から $S$ へも到達できる）ため、$S$ と $S'$ の両方から探索を行う必要はないためです。逆に他のマスから到達されなかった場合でも、自身から到達できるマスの数を求める必要があるため、少なくとも $1$ 回は登場します。

磁石と隣接しているマス $T'$ については、高々 $4$ 回しか登場しません。$T'$ 自身からスタートとなっている場合を除くと、必ず他の隣接するマスから移動することによって登場します。しかしこの $T'$ に移動してくる直前のマスは（$T'$ に移動できていることから）磁石と隣接していないマスであり、探索に一度しか登場しません。よって、各隣接するマスから $T'$ に到達される回数は高々 $1$ 回です。$T'$ は高々 $4$ つのマスとしか隣接しておらず少なくとも $1$ つには磁石が置かれていることから、他のマスから $T'$ への移動は高々 $3$ 回です。自身をスタートとする場合を合わせても高々 $4$ かいとなります。

ゆえに、（移動を開始したマス, そこから到達できたマス）のペアは高々 $O(HW)$ 個しか登場せず、全体で $O(HW)$ の計算量で解くことができ、これは十分に高速です。
よって、この問題を解くことができました。

なお、この問題は自由度を求めるマスをランダムに選ぶ乱択アルゴリズムを用いても十分に高い確率で正答を得ることができます。

c++ による実装例: -->

# D - Grid and Magnet

First, let's consider how to determine the freedom of the cells where magnets are not placed.
This can be done, for example, by performing depth-first search on a grid graph.
Consider each cell where a magnet is not placed as a vertex (hereinafter referred to as vertex $A$ corresponding to cell $A$), and consider a graph where there is an edge from vertex $A$ to vertex $B$ if you can move from cell $A$ to cell $B$ in one step, and only then. By traversing the edges from vertex $S$ using depth-first search, we can enumerate the vertices reachable from vertex $S$ and count their number. (Breadth-first search is also acceptable.) By doing this for all (unoccupied by magnets) cells, we can obtain the answer.

However, here, since the graph has a maximum of $O(HW)$ vertices and edges, determining the freedom of a single cell requires $O(HW)$ computations, and in the worst case, it will take $O(H^2 W^2)$ computations overall, making it difficult to meet the time limit.

Therefore, let's focus on the fact that if you can move from cell $A$ to cell $B$, and cell $B$ is not adjacent to a cell where a magnet is placed, then the freedom of cell $A$ and cell $B$ is equal. This is because when cell $B$ is not adjacent to a cell where a magnet is placed, you can reach cell $A$ from cell $B$ by retracing the path taken from cell $A$ to cell $B$, and at this time, for any other cell $C$, the ability to reach cell $C$ from cell $A$ is equivalent to the ability to reach cell $C$ from cell $B$. Therefore, during the exploration of cells reachable from a certain cell $S$, if we encounter a cell $S'$ that is not adjacent to a magnet, we do not need to re-examine the number of cells reachable from cell $S'$ starting from scratch, as it has already been explored at least once. This can be managed by keeping a flag indicating whether the cell has been explored before.

Let's consider the computational complexity when doing this. Since the number of edges extending from each vertex is constant, the time complexity essentially depends on the number of pairs of (cell where the movement started, cell reached from there) encountered during the search.

Focusing on the latter, let's consider how many times each cell appears as a "cell reached from there". For a cell $T$ not adjacent to a magnet, it appears exactly once. This is because if we visit cell $T$ more than twice, we are conducting a search where cell $T$ is reached from two different cells $S$ and $S'$, but since cell $T$ can be reached from cell $S$ via cell $T$ (and similarly from cell $S'$ to cell $S$), we do not need to conduct searches from both $S$ and $S'$. Conversely, even if it is not reached from other cells, we need to determine the number of cells reachable from itself, so it appears at least once.

For a cell $T'$ adjacent to a magnet, it appears at most four times. Except when $T'$ is the starting point itself, it always appears by moving from other adjacent cells. However, just before moving to $T'$ (since it is possible to move to $T'$), the cell is not adjacent to a magnet and only appears once in the search. Therefore, the number of times each adjacent cell reaches $T'$ is at most once. Since $T'$ is adjacent to at most four cells and at least one of them has a magnet, the number of movements from other cells to $T'$ is at most three. Even when including the case where it starts from itself, it is at most four times.

Therefore, the pairs of (cell where the movement started, cell reached from there) appear at most $O(HW)$ times in total, and the problem can be solved with a computational complexity of $O(HW)$, which is sufficiently fast. Thus, we have solved this problem.

Additionally, this problem can be solved with a high probability of correctness using a randomized algorithm that randomly selects the cells for which to determine the freedom.

Example Implementation in C++:

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int>e[1000000];
int used[1000000];
int cnt;

void dfs(int s,int v){
	if(used[v]==s)return;
	used[v]=s;
	cnt++;
	int sz=e[v].size();
	for(int i=0;i<sz;i++)dfs(s,e[v][i]);
	return;
}

int main(void){
	int dx[4]={0,0,1,-1};
	int dy[4]={1,-1,0,0};
	int h,w,ans=0;
	bool can;
	cin>>h>>w;
	vector<string>s(h);
	for(int i=0;i<h;i++)cin>>s[i];
	for(int i=0;i<h;i++){
		for(int j=0;j<w;j++){
			if(s[i][j]=='#')continue;
			can=true;
			for(int k=0;k<4;k++){
				if((i+dx[k]>=0)&&(i+dx[k]<h)&&(j+dy[k]>=0)&&(j+dy[k]<w)){
					e[i*w+j].push_back((i+dx[k])*w+(j+dy[k]));
					if(s[i+dx[k]][j+dy[k]]=='#')can=false;
				}
			}
			if(!can){
				e[i*w+j].clear();
				continue;
			}
		}
	}
	for(int i=0;i<(h*w);i++)used[i]=-1;
	for(int i=0;i<h;i++){
		for(int j=0;j<w;j++){
			if((s[i][j]=='.')&&(used[i*w+j]<0)){
				cnt=0;
				dfs(i*w+j,i*w+j);
				ans=max(ans,cnt);
			}
		}
	}
	cout<<ans<<endl;
}

```

```cpp
#include <bits/stdc++.h>
using namespace std;

using P = pair<int, int>;
int di[] = {-1, 0, 1, 0};
int dj[] = {0, -1, 0, 1};
int main(){
    int H, W; cin >> H >> W;
    vector<string> S(H);
    for (int i = 0; i < H; i++) cin >> S[i];
    vector x(H, vector<bool>(W));
    for (int i = 0; i < H; i++){
        for (int j = 0; j < W; j++){
            if (S[i][j] == '#'){
                x[i][j] = true;
                for (int v = 0; v < 4; v++){
                    int ni = i + di[v], nj = j + dj[v];
                    if (ni < 0 || ni >= H || nj < 0 || nj >= W) continue;
                    x[ni][nj] = true;
                }
            }
        }
    }
    vector used(H, vector<bool>(W));
    vector last(H, vector<int>(W)); int tm = 0;
    int ans = 1;
    for (int si = 0; si < H; si++){
        for (int sj = 0; sj < W; sj++){
            if (!x[si][sj]){
                if (used[si][sj]) continue;
                ++tm;
                int cnt = 0;
                queue<P> q;
                q.emplace(si, sj);
                used[si][sj] = true;
                while (!q.empty()){
                    auto [i, j] = q.front(); q.pop();
                    cnt++;
                    for (int v = 0; v < 4; v++){
                        int ni = i + di[v], nj = j + dj[v];
                        if (ni < 0 || ni >= H || nj < 0 || nj >= W) continue;
                        if (used[ni][nj]) continue;
                        if (x[ni][nj]){
                            if (last[ni][nj] != tm) cnt++, last[ni][nj] = tm;
                            continue;
                        }
                        q.emplace(ni, nj);
                        used[ni][nj] = true;
                    }
                }
                ans = max(ans, cnt);
            }
        }
    }
    cout << ans << endl;
    return 0;
}
```
