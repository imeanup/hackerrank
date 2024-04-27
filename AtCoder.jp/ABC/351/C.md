# C - Merge the balls

<!-- それぞれの操作を順にシミュレーションすることを考えます。

ここで、$N$ 個のボールの大きさはすべて $2$ のべき乗であり、手順において取り除かれたボールの大きさが $2$ のべき乗であるとき、新たに付け加えられるボールの大きさも $2$ のべき乗となることから、登場するボールの大きさはすべて $2$ のべき乗です。
また、$X = Y$ と $2^X = 2^Y$ が同値であることから、ボールの大きさの代わりにボールの大きさの（$2$ を底とした）対数を管理すれば十分です。

具体的には列にあるボールの数 $L$ と 列にあるボールの大きさの対数を左から順に並べたもの $S = (S_1, S_2, \cdots, S_L)$ を管理しておき、これを更新していくことを考えます。
最初は $L = 0$, $S = ()$（空の列）です。

$i$ 個目のボールを列の一番右に付け加える操作は $L \gets (L+1)$ とし、$S$ の末尾に $A_i$ をつけ加えれば良いです。

その後の手順は、列の大きさが $2$ 以上である限り、「$S$ の末尾から $2$ つの要素  $S_{L-1}$ を取り出して大きさを比較し、異なれば元に戻して操作を終了し、等しければ（すなわち$S_{L-1} = S_L = X$ であれば ）、 $L \gets (L-1)$ として $S$ の末尾に $(X+1)$ を加えて再度この手順を行う」ことを繰り返せば良いです。ここで、$2^X+2^X=2^{X+1}$ であることに注意してください。$N$ 回の操作が終了した後の $L$ の値が答えとなります。

次に、計算量について考えます。前者の $i$ 個目（$1 \le i \le N$）のボールを列の一番右に付け加える操作はちょうど $N$ 回行われます。後者の手順について、「 $2$ つのボールを取り出して $1$ つを加える」という操作は列のボールの数を $1$ 減少させるため、 $N$ 回の操作の中で高々 $(N-1)$ 回しか行うことができません。よって、列にボールを取り出す・加えるという操作はそれぞれ高々 $O(N)$ 回しか行われません。

それぞれの操作は配列で行うこともできますし、スタック等で管理することもできます。いずれの場合も末尾に付け加えたり取り除く操作は $O(1)$ でおこなうことができます。よって、シミュレーションに必要な時間計算量は全体で $O(N)$ であり十分高速です。よって、この問題を解くことができました。

c++ による実装例: -->

<!-- Consider simulating each operation in turn.

Here, the size of all $N$ balls is a power of $2$, and when the size of the ball removed in the procedure is a power of $2$, the size of the newly added ball is also a power of $2$. Since it is a power, the size of the balls that appear are all powers of $2$.
Also, since $X = Y$ and $2^X = 2^Y$ are equivalent, it is sufficient to manage the logarithm of the ball size (base $2$) instead of the ball size. .

Specifically, we manage the number of balls in a row $L$ and the logarithm of the size of balls in a row from left to right, $S = (S_1, S_2, \cdots, S_L)$. I'm thinking of updating this.
Initially $L = 0$, $S = ()$ (empty column).

To add the $i$-th ball to the right end of the column, use $L \gets (L+1)$ and add $A_i$ to the end of $S$.

The next step is to extract $2$ elements $S_{L-1}$ from the end of $S$, compare the sizes, and return them if they are different, as long as the size of the column is greater than or equal to $2$. If they are equal (i.e. if $S_{L-1} = S_L = X$ ), $L \gets (L-1)$ returns $(X+1) to the end of $S$ Just add $ and repeat this step again. Note here that $2^X+2^X=2^{X+1}$. The answer is the value of $L$ after $N$ operations.

Next, consider the amount of calculation. The former operation of adding the $i$th ball $(1 \le i \le N)$ to the rightmost part of the column is performed exactly $N$ times. Regarding the latter procedure, the operation "take out $2$ balls and add $1$" reduces the number of balls in the row by $1$, so in $N$ operations, at most $(N-1)$ Can only be done $ times. Therefore, each operation of taking out and adding balls to a column is performed at most $O(N)$ times.

Each operation can be performed using an array or managed using a stack, etc. In either case, adding or removing from the end can be done in $O(1)$. Therefore, the total amount of time required for simulation is $O(N)$, which is sufficiently fast. Therefore, I was able to solve this problem.

Example implementation in c++: -->

## Solution

Let's consider simulating each operation sequentially.

Here, since the size of each of the $N$ balls is a power of $2$, and when a ball of size $2$ to the power of $X$ is removed during a step, the size of newly ball added is also a power of $2$, all the sizes of the balls involved are powers of $2$. Additionally, since $X = Y$ and $2^X = 2^Y$ are equivalent, it is sufficient to manage the logarithms (base $2$) of the sizes of the balls instead of the sizes themselves.

Specifically, let's maintain the number of balls $L$ in the column and the logarithm of the sizes of the balls in the column, arranged from left to right, as $S = (S_1, S_2, \cdots, S_L)$, and consider updating it.
Initially, $L = 0$ and $S = ()$ (an empty column).

The operation to add the $i$-th ball to the right end of the column is $L \gets (L+1)$, and it suffices to append $A_i$ to the end of $S$.

Subsequently, as long as the size of the column is greater than or equal to $2$, the following procedure is repeated: "Take out the last two elements $S_{L-1}$ from $S$ and compare their sizes. If they are different, revert them and end the operation; if they are the same (i.e., $S_{L-1} = S_L = X$), then set $L \gets (L-1)$ and add $(X+1)$ to the end of $S$ and repeat this procedure." Note that $2^X+2^X=2^{X+1}$. The value of $L$ after $N$ operations have been completed is the answer.

Next, let's consider the computational complexity. The former operation of adding the $i$-th ball to the right end of the column (for $1 \leq i \leq N$) is performed exactly $N$ times. Regarding the latter procedure, the operation of "taking out two balls and adding one" reduces the number of balls in the column by $1$, so it can be performed at most $(N-1)$ times within $N$ operations. Therefore, the operations of removing and adding balls to the column are performed at most $O(N)$ times each.

These operations can be performed using arrays or managed with stacks, etc. In either case, operations such as appending or removing from the end can be done in $O(1)$. Therefore, the time complexity required for simulation is overall $O(N)$, which is sufficiently fast. Thus, we have solved this problem.

Example Implementation in C++:


```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, l = 0; cin >> N;
    int A[200005];
    for (int i = 0; i < N; i++){
        cin >> A[l];
        l++;
        while (l > 1){
            if (A[l-1] == A[l-2]){
                A[l-2]++;
                l--;
            }
            else {
                break;
            }
        }
    }
    cout << l << endl;
    return 0;
}
```

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, l = 0; cin >> N;
    vector<int> A(N); 
    for (int i = 0; i < N; i++) cin >> A[i];
    stack <int> st;

    for (int a : A){
        while (!st.empty() && st.top() == a){
            int now = st.top();
            st.pop();
            a = now + 1;
        }
        st.push(a);
    }

    cout << st.size() << "\n";
    return 0;
}
```
