# Algorithm for Computing the Shortest Path Length with $d$ Edges on a Monge Graph

## Overview

Consider a complete DAG (Directed Acyclic Graph) $G = (N, E = \{ (i, j) \mid i < j \})$ with $N$ vertices, where $c : E \to \mathbb{Z}$ represents edge weights that satisfy the Monge property, and let $d$ be a positive integer. The problem is to compute the shortest path length from vertex $0$ to vertex $N-1$ using exactly $d$ edges.

This is a constrained optimization problem, and its strong duality with the Lagrangian dual problem is guaranteed by the Monge property of $c$. Utilizing this strong duality, the problem can be reduced to solving the Lagrangian relaxation problem $\Theta(\log (\max_{e \in E} \lvert c(e) \rvert))$ times.

The Lagrangian relaxation problem transforms into a shortest path problem without edge count constraints when all edge weights are uniformly increased by $\lambda$. If $c$ is Monge, adding a uniform $\lambda$ to all edge weights preserves the Monge property. The shortest path with Monge edge weights can be computed in $\Theta(N)$ time using the LARSCH Algorithm[^LARSCH].

Therefore, the shortest path length with $d$ edges on a Monge graph can be computed in $\Theta(N \log (\max_{e \in E} \lvert c(e) \rvert))$ time.

The Aliens[^Aliens] problem can be reduced to this problem. Consequently, the approach using Lagrangian relaxation is sometimes referred to as Alien DP[^kort0n-AlienDP]. It is also known as WQS binary search[^WQS-binary-search].

## Monge Property

In this article, the edge weights $c : E \to \mathbb{Z}$ are said to satisfy the Monge property if

$$\forall i, j, k, l.\  0 \leq i < j < k < l < N \rightarrow c(i, l) + c(j, k) \geq c(i, k) + c(j, l)$$

The Monge property is typically defined for $M \times N$ matrices, but here it is defined in a restricted form for the upper triangular part of the matrix $c$.

## Lagrangian Dual Problem

Let $\mathcal{P}$ denote the set of all $0$-$(N - 1)$ paths in $G$.
For $P \in \mathcal{P}$, let $\lVert P \rVert$ represent the number of edges in $P$, and $c(P)$ the sum of the edge weights of $P$.

The value we want to find is $\displaystyle \min_{P \in \mathcal{P}, \lVert P \rVert = d} c(P)$.

For any $\lambda \in \mathbb{Z}$, the following equation holds:

$$
\begin{aligned}
  \min_{P \in \mathcal{P}, \lVert P \rVert = d} c(P) & = \min_{P \in \mathcal{P}, \lVert P \rVert = d} (c(P) + \lambda (\lVert P \rVert - d)) \cr
  & \geq \min_{P \in \mathcal{P}} (c(P) + \lambda (\lVert P \rVert - d))
\end{aligned}
$$

This reformulation, where part of the constraints is removed and the violation of the removed constraint is incorporated into the objective function as a linear penalty[^lagrangian-penalty], is called the Lagrangian relaxation problem[^lagrangian-relaxation]. The solution to the Lagrangian relaxation problem provides a lower bound to the original problem.

From (1), the following equation holds:

$$
\begin{equation}
  \min_{P \in \mathcal{P}, \lVert P \rVert = d} c(P) \geq \max_{\lambda \in \mathbb{Z}} \min_{P \in \mathcal{P}} (c(P) + \lambda (\lVert P \rVert - d))
\end{equation}
$$

This can be interpreted as finding the best lower bound by adjusting $\lambda$.
The problem of finding this best lower bound is called the Lagrangian dual problem.

In general, the equality does not necessarily hold in (2), but in the setting of this problem, the equality holds.
The situation where the solutions to the primal problem and the dual problem coincide is called strong duality.
The main purpose of the following lemma is to demonstrate strong duality (Theorem 3).

Define $P_k^*$ as the shortest path from $0$ to $(N-1)$ using exactly $k$ edges.
If multiple such paths exist, choose one arbitrarily.

### Lemma 1

$$\forall k.\ 2 \leq k \leq N - 2 \rightarrow c(P_k^\ast) - c(P_{k-1}^\ast) \leq c(P_{k+1}^\ast) - c(P_k^\ast)$$

#### Proof

We need to show the existence of paths $P, P' \in \mathcal{P}$ with $\lVert P \rVert = \lVert P' \rVert = k$ such that $c(P_{k-1}^\ast) + c(P_{k+1}^\ast) \geq c(P) + c(P')$. If this is established, the desired inequality follows by rearranging $c(P_{k-1}^\ast) + c(P_{k+1}^\ast) \geq c(P) + c(P') \geq c(P_k^\ast) + c(P_k^\ast)$.

Represent the paths as sequences of vertices. Let

$$
P_{k-1}^\ast = (s_0, s_1, \dots, s_{k-1}) \quad \text{and} \quad P_{k+1}^\ast = (t_0, t_1, \dots, t_{k+1})
$$

where $s_0 = t_0 = 0$ and $s_{k-1} = t_{k+1} = N - 1$. 

For each $0 \leq x \leq k - 1$, compare $s_x$ and $t_{x+1}$. Since $s_0 < t_1$ and $s_{k-1} > t_k$, there either exists an $x$ such that $s_x = t_{x+1}$, or there exists an $x$ such that $s_x < t_{x+1}$ and $s_{x+1} > t_{x+2}$.

- **If there exists an $x$ such that $s_x = t_{x+1}$**:

    Define
    $$
    \begin{aligned}
      P &\coloneqq (s_0, s_1, \dots, s_x, t_{x+2}, t_{x+3}, \dots, t_{k+1}) \cr
      P' &\coloneqq (t_0, t_1, \dots, t_{x+1}, s_{x+1}, s_{x+2}, \dots, s_{k-1})
    \end{aligned}
    $$
    Then $c(P_{k-1}^\ast) + c(P_{k+1}^\ast) = c(P) + c(P')$.

- **If there exists an $x$ such that $s_x < t_{x+1}$ and $s_{x+1} > t_{x+2}$**:

    Then, we have $s_x < t_{x+1} < t_{x+2} < s_{x+1}$. Define
    $$
    \begin{aligned}
      P &\coloneqq (s_0, s_1, \dots, s_x, t_{x+2}, t_{x+3}, \dots, t_{k+1}) \cr
      P' &\coloneqq (t_0, t_1, \dots, t_{x+1}, s_{x+1}, s_{x+2}, \dots, s_{k-1})
    \end{aligned}
    $$
    From the Monge property of $c$, we have $c(s_x, s_{x+1}) + c(t_{x+1}, t_{x+2}) \geq c(s_x, t_{x+2}) + c(t_{x+1}, s_{x+1})$, which implies $c(P_{k-1}^\ast) + c(P_{k+1}^\ast) \geq c(P) + c(P')$.

$\blacksquare$

Lemma 1 indicates that the function $k \mapsto c(P_k^\ast)$ is convex.

### Lemma 2

There exist $\lambda^\ast \in \mathbb{Z}$ and $P^\ast \in \mathcal{P}$ such that $\displaystyle \lVert P^\ast \rVert = d \land P^\ast \in \argmin_{P \in \mathcal{P}} (c(P) + \lambda^\ast (\lVert P \rVert - d))$.

#### Proof

Using Lemma 1, choose $\lambda^\ast$ such that $- (c(P_{d+1}^\ast) - c(P_d^\ast)) \leq \lambda^\ast \leq - (c(P_d^\ast) - c(P_{d-1}^\ast))$. If we can show that $\forall k.\ c(P_k^\ast) + \lambda^\ast (k - d) \geq c(P_d^\ast)$, then $\displaystyle P_d^\ast \in \argmin_{P \in \mathcal{P}} (c(P) + \lambda^\ast (\lVert P \rVert - d))$, and we can take $P^\ast$ to be $P_d^\ast$.

- For $k < d$:

    $$ \begin{aligned}
      c(P_k^\ast) + \lambda^\ast (k - d)
      & = c(P_d^\ast) - \sum_{i=k}^{d-1} (c(P_{i+1}^\ast) - c(P_i^\ast)) + \lambda^\ast (k - d) \cr
      & \geq c(P_d^\ast) - (c(P_d^\ast) - c(P_{d-1}^\ast)) (d - k) + \lambda^\ast (k - d) & & (\text{by Lemma 1}) \cr
      & \geq c(P_d^\ast) + \lambda^\ast (d - k) + \lambda^\ast (k - d) & & (\text{by the definition of } \lambda^\ast) \cr
      & = c(P_d^\ast)
    \end{aligned} $$

- For $k \geq d$:

    $$ \begin{aligned}
      c(P_k^\ast) + \lambda^\ast (k - d)
      & = c(P_d^\ast) + \sum_{i=d}^{k-1} (c(P_{i+1}^\ast) - c(P_i^\ast)) + \lambda^\ast (k - d) \cr
      & \geq c(P_d^\ast) + (c(P_{d+1}^\ast) - c(P_d^\ast)) (k - d) + \lambda^\ast (k - d) & & (\text{by Lemma 1}) \cr
      & \geq c(P_d^\ast) - \lambda^\ast (k - d) + \lambda^\ast (k - d) & & (\text{by the definition of } \lambda^\ast) \cr
      & = c(P_d^\ast)
    \end{aligned} $$

$\blacksquare$

### Theorem 3

$$
  \min_{P \in \mathcal{P}, \lVert P \rVert = d} c(P) = \max_{\lambda \in \mathbb{Z}} \min_{P \in \mathcal{P}} (c(P) + \lambda (\lVert P \rVert - d))
$$

### Proof

Using Lemma 2, we take $\lambda^\ast$ and $P^\ast$ such that $\displaystyle \lVert P^\ast \rVert = d$ and $P^\ast \in \argmin_{P \in \mathcal{P}} (c(P) + \lambda^\ast (\lVert P \rVert - d))$.

$$ \begin{aligned}
  \min_{P \in \mathcal{P}, \lVert P \rVert = d} c(P) & \leq c(P^\ast) \cr
  & = c(P^\ast) + \lambda^\ast (\lVert P^\ast \rVert - d) \cr
  & = \min_{P \in \mathcal{P}} (c(P) + \lambda^\ast (\lVert P \rVert - d)) \cr
  & \leq \max_{\lambda \in \mathbb{Z}} \min_{P \in \mathcal{P}} (c(P) + \lambda (\lVert P \rVert - d))
\end{aligned} $$

Combining this with $(2)$ establishes the desired equality.
\(\blacksquare\)

## Algorithm

Solve the Lagrangian dual problem $\displaystyle \max_{\lambda \in \mathbb{Z}} \min_{P \in \mathcal{P}} (c(P) + \lambda (\lVert P \rVert - d))$. Since $\displaystyle L: \lambda \mapsto \min_{P \in \mathcal{P}} (c(P) + \lambda (\lVert P \rVert - d))$ is a convex function, its maximum can be found using ternary search. According to Theorem 3, the maximum value of $L$ is the desired output $\displaystyle \min_{P \in \mathcal{P}, \lVert P \rVert = d} c(P)$.

The remaining task is to compute $L(\lambda)$ for a given $\lambda$. Define edge weights $c_{\lambda}: E \to \mathbb{Z}$ by $c_{\lambda}(e) = c(e) + \lambda$. This means that $c_{\lambda}$ is the weight $c$ increased by $\lambda$ for every edge. Then, we can rewrite:
$$ \begin{aligned}
  L(\lambda)
  & = \min_{P \in \mathcal{P}} (c(P) + \lambda (\lVert P \rVert - d)) \cr
  & = \min_{P \in \mathcal{P}} (c(P) + \lambda \lVert P \rVert - \lambda d) \cr
  & = - \lambda d + \min_{P \in \mathcal{P}} c_{\lambda}(P)
\end{aligned} $$
Therefore, we can obtain the value of $L(\lambda)$ by computing the shortest path length under $c_{\lambda}$.

Since $c$ is Monge, $c_{\lambda}$ is also Monge. The shortest path in a complete DAG with Monge edge weights can be computed in $\Theta(N)$ time using the LARSCH Algorithm[^LARSCH]. In Aliens[^Aliens], the properties of $c_{\lambda}$ are even better, allowing the shortest path to be computed in $\Theta(N)$ time using the Convex Hull Trick.

Setting $\lambda = - 3 \max_{e \in E} |c(e)|$ ensures that the path with $N - 1$ edges is the shortest. For smaller values of $\lambda$, $L(\lambda)$ monotonically decreases, so $- 3 \max_{e \in E} |c(e)|$ can be used as the lower bound for ternary search. Similarly, $3 \max_{e \in E} |c(e)|$ can be used as the upper bound.

The overall time complexity is $\Theta(N \log (\max_{e \in E} |c(e)|))$.

## Additional Notes

-    If $c(e)$ is input for all $e \in E$, the time complexity would become $\Theta(N^2)$. Therefore, the algorithm's time complexity is evaluated under the assumption that $c(i, j)$ can be computed in $\Omicron(1)$ time when given $i$ and $j$.
-    There is another method that focuses on the monotonic decrease of $\lVert P \rVert$ with respect to $\lambda$ for the $P$ that minimizes $c_{\lambda}(P)$. This method finds $\lambda$ such that $\lVert P \rVert = d$ exactly through binary search[^exact]. This is essentially equivalent to maximizing $L$ through binary search on the slope.
-   The shortest path length with the condition of using at most $d$ edges can also be computed. From Lemma 1, we know that $k \mapsto c(P_k^\ast)$ is convex. Therefore, the potential shortest paths under the condition of using at most $d$ edges are either the shortest path without any conditions or $P_d^\ast$. The case for using at least $d$ edges can be computed similarly.

## References

-   Bein, W. W., Larmore, L. L., & Park, J. K. (1992). The d-edge shortest-path problem for a Monge graph (No. SAND-92-1724C; CONF-930194-1). Sandia National Labs., Albuquerque, NM (United States).

-   [Yoichi Iwata (NII) (2018). Duality. JOI Spring Camp.](https://www.slideshare.net/wata_orz/ss-91375739) <sup>[archive.org](https://web.archive.org/web/20201101134907/https://www.slideshare.net/wata_orz/ss-91375739)</sup>

## Notes

[^Aliens]: [IOI 2016 Aliens](https://ioinformatics.org/files/ioi2016problem6.pdf) <sup>[archive.org](https://web.archive.org/web/20191021104945/https://ioinformatics.org/files/ioi2016problem6.pdf)</sup>

[^kort0n-AlienDP]: Tweet by <a class="handle">kort0n</a> <https://twitter.com/kyort0n/status/1260986271314227206><sup>[archive.org](https://web.archive.org/web/20200514195641/https://twitter.com/kyort0n/status/1260986271314227206)</sup>

[^lagrangian-penalty]: Since $\lambda (\lVert P \rVert - d)$ can be negative, interpreting it as a penalty can be difficult. Refer to the equation transformation for a precise discussion.
[^lagrangian-relaxation]: [Lagrangian Relaxation Problem - Mathematical Programming Glossary](http://www.msi.co.jp/nuopt/glossary/term_c4995faa151e2d66d8ea36c8eaff94885d60c19f.html) <sup>[archive.org](https://web.archive.org/web/20200221035313/http://www.msi.co.jp/nuopt/glossary/term_c4995faa151e2d66d8ea36c8eaff94885d60c19f.html)</sup>

[^LARSCH]: Larmore, L. L., & Schieber, B. (1991). On-line dynamic programming with applications to the prediction of RNA secondary structure. Journal of Algorithms, 12(3), 490-515.

[^exact]: Strictly speaking, if there are multiple $P$ that minimize $c_{\lambda}(P)$, there may not be a $\lambda$ that exactly satisfies the condition. In such cases, appropriate reconstruction or adjustments are necessary.

[^WQS-binary-search]: [DP Optimization - WQS Binary Search Optimization | A Simple Blog](https://robert1003.github.io/2020/02/26/dp-opt-wqs-binary-search.html) <sup>[archive.org](https://web.archive.org/web/20210326063417/https://robert1003.github.io/2020/02/26/dp-opt-wqs-binary-search.html)</sup>　<https://codeforces.com/blog/entry/49691?#comment-402636> <sup>[archive.org](https://web.archive.org/web/20210326064207/https://codeforces.com/blog/entry/49691)</sup>

Translated from [here](https://noshi91.github.io/algorithm-encyclopedia/d-edge-shortest-path-monge)
