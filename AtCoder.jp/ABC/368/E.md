## [E - Train Delay](https://atcoder.jp/contests/abc368/tasks/abc368_e)

<details style="border: 1px solid black; padding: 10px;"><summary><b>Japanese</b></summary><br>

$S_i, T_i$ を「時刻表上の発車・到着時刻」、$S_i+X_i,T_i+X_i$ を「実際の発車・到着時刻」と呼ぶことにします。

電車の発車を遅らせても他の電車の発車を早めることはできないため、全ての電車は発車可能な最も早い時刻に発車するとしてよいです。

ある電車 $i$ が発車可能かどうかに影響するのは、時刻表上の到着時刻が電車 $i$ の時刻表上の発車時刻より前の電車に限ります。よって、時刻表上の発車・到着時刻の順に電車を処理することでうまくいきそうです。

実際、$2M$ 個の発車・到着イベントを時刻表上の発車・到着時刻の順に ソートしたあと、順に次のような処理を行うことで処理できます。

* 電車 $i$ が発車する際には、現在までに処理した電車（すなわち時刻表上の到着時刻が電車 $i$ の時刻表上の発車時刻までの電車）の駅 $A_i$ への実際の到着時刻に基づいて $X_i$ を計算する
* 電車 $i$ が到着する際には、$X_i$ に基づいて、駅 $B_i$ に実際に到着した到着時刻を記録する

これらの処理は、各駅 について「現在までに到着処理を行った電車のうち、もっとも遅い実際の到着時刻」を管理することで、どちらも $O(1)$ で行うことができます。

発車と到着が同じ時刻に起こる際は、到着の処理を先に行う必要があることに注意してください。

```py
N,M,X=map(int,input().split())
A,B,S,T=zip(*[tuple(map(int,input().split())) for _ in range(M)])

event=sorted([(S[i],1,i) for i in range(M)] + [(T[i],0,i) for i in range(M)])

ans=[0]*M
ans[0]=X

station=[0]*(N+1)
for t,f,i in event:
  if f:
    # 出発　駅A[i]に来るのが最も遅い電車に合わせて発車する（電車1以外）
    if i:
      ans[i]=max(0,station[A[i]]-t)
  else:
    # 到着　駅B[i]に着いた最も遅い電車の情報を更新する
    station[B[i]]=max(station[B[i]],t+ans[i])

print(*ans[1:])
```

</details><br>

### Translation of the Explanation:

We refer to $S_i$ and $T_i$ as the "scheduled departure and arrival times" and $S_i + X_i$ and $T_i + X_i$ as the "actual departure and arrival times."

Since delaying a train's departure cannot cause another train to depart earlier, we can assume that all trains will depart at the earliest possible time.

The only trains that can affect whether a given train $i$ can depart are those whose scheduled arrival times are before the scheduled departure time of train $i$. Therefore, processing the trains in the order of their scheduled departure and arrival times should work well.

In practice, we can handle the problem by sorting the $2M$ departure and arrival events by their scheduled times and then processing them in order as follows:

* When train $i$ departs, calculate $X_i$ based on the actual arrival times of the trains that have already been processed (i.e., those whose scheduled arrival times are up to the scheduled departure time of train $i$ at station $A_i$).
* When train $i$ arrives, update the actual arrival time at station $B_i$ based on $X_i$.

These operations can both be done in $O(1)$ time by maintaining "the latest actual arrival time" for each station.

Note that when departure and arrival happen at the same time, the arrival should be processed first.

<details style="border: 1px solid black; padding: 10px;"><summary>C++</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;

int main() {
    int N, M, X;
    cin >> N >> M >> X;

    vector<int> A(M), B(M), S(M), T(M);
    for (int i = 0; i < M; ++i) {
        cin >> A[i] >> B[i] >> S[i] >> T[i];
    }

    // Create events and sort them
    vector<tuple<int, int, int>> event;
    for (int i = 0; i < M; ++i) {
        event.emplace_back(S[i], 1, i); // Departure event
        event.emplace_back(T[i], 0, i); // Arrival event
    }
    sort(event.begin(), event.end());

    vector<int> ans(M, 0);
    ans[0] = X;

    vector<int> station(N + 1, 0); // Record the latest actual arrival time at each station
    for (const auto& [t, f, i] : event) {
        if (f == 1) {
            // Departure: Set the departure time according to the latest arrival at station A[i]
            if (i != 0) {
                ans[i] = max(0, station[A[i]] - t);
            }
        } else {
            // Arrival: Update the latest arrival time at station B[i]
            station[B[i]] = max(station[B[i]], t + ans[i]);
        }
    }

    for (int i = 1; i < M; ++i) {
        cout << ans[i] << " ";
    }
    cout << endl;

    return 0;
}
```

</details><br>
