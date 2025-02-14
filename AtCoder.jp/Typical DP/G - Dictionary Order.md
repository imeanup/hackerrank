# [G - Dictionary Order](https://atcoder.jp/contests/tdpc/tasks/tdpc_lexicographical)

> Time Limit: 2 sec / Memory Limit: 256 MB

### Problem Statement

<!-- 文字列 $s$ の空でない部分列のうち、辞書順で $K$ 番目のものを求めよ。そのようなものが存在しない場合は "Eel" (quotes for clarity) と出力せよ。

ただし、$s$ から何文字か取り除き (0 文字でもよい)、残りの文字を順番を変えずにつなげたものを部分列という。たとえば、"aba" の部分列は "a", "b", "aa", "ab", "ba", "aba" の 6 個である。"a" は異なる場所に二回現れるが、文字列として同じであれば区別しないものとする。 -->

Find the $K$-th lexicographically smallest non-empty subsequence of the string $s$. If such a subsequence does not exist, output "Eel" (quotes for clarity).

A subsequence is formed by removing some characters (possibly $0$) from $s$ and concatenating the remaining characters in order. For example, the subsequences of “aba” are "a", "b", "aa", "ab", "ba", and "aba". If the same character appears more than once at different positions, they are not distinguished from each other as long as the resulting string is the same.


### Constraints

* $1 \le |s| \le 1000000$
* Each character in s will be a lowercase letter ('a'-'z').
* $1 \le K \le 10^{18}$

---

### Input Format

<!-- 入力は以下の形式で標準入力から与えられる。 -->
Input is given from standard input in the following format:

$s \\ K$

### Output Format

<!-- 答えを一行に出力せよ。 -->
Print the answer on one line.

---

### Sample Input 1

```
eel
6
```

### Sample Output 1

```
Eel
```

<!-- eel の部分列は辞書順に e, ee, eel, el, l である。6 番目は存在しない。 -->
The subsequences of eel, in lexicographical order, are e, ee, eel, el, l. There is no sixth.

---

### Sample Input 2

```
lexicographical
100
```

### Sample Output 2

```
capal
```
