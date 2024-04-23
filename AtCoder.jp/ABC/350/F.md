## [F - Transpose](https://atcoder.jp/contests/abc350/tasks/abc350_f)
<!-- 
一度に全ての操作を考えると混乱のもとなので、手の付けやすい複数の操作に分解することもひとつの手です。

まず、最終的な文字列の大文字小文字について判定しましょう。
これはそれほど難しくなく、以下のように判定できます。

* 括弧列の深さが **偶数** であるところに位置する文字は、大文字小文字が **反転しない。**
* 括弧列の深さが **奇数** であるところに位置する文字は、大文字小文字が **反転する。**

これに従って予め文字の大小を入れ替えておくことで、これ以上文字の大小を考える必要はなくなりました。

いま、考えるべきは次のような操作です。

* 先頭と末尾がそれぞれ `(` と `)` であるような連続部分列について、 `(` と `)` とを取り除いたうえで文字列を反転させる

最終的な文字列は以下のような再帰で求めることが可能です。

* $f(l, r, d)$ という再帰関数を定義する。
* $d = 0$ のとき、 $l, l+1, \cdots, r$ 文字目の順に調べ、英文字が出てきたらその都度出力する。
  * その途中 $l_u$ 文字目に `(` を発見した時、それに対応する `)` を $r_u$ 文字目とする。
  * このとき、 $f(l_u + 1, r_u - 1, 1)$ を呼び、その後 $r_u + 1$ 文字目から処理を続行する。 ( $r_u + 1$ 文字目以降が出力されるのは $l_u$ 文字目から $r_u$ 文字目までの処理が終わった後であることに注意せよ。)
* $d = 1$ のとき、 $r, r-1, \cdots, l$ 文字目の順に調べ、英文字が出てきたらその都度出力する。
  * その途中 $r_u$ 文字目に `)` を発見した時、それに対応する `(` を $l_u$ 文字目とする。
  * このとき、 $f(l_u + 1, r_u - 1, 0)$ を呼び、その後 $l_u-1$ 文字目から処理を続行する。

対応する `(` と `)` は予計算により時間計算量 $O(|S|)$ で求めることができます。
あとは、 $f(1,∣S∣,0)$ を呼び出すことで、この問題に時間計算量 $O(∣S∣)$ で正解できます。

実装例 (C++) : -->

Breaking down the operations into more manageable components can be helpful to avoid confusion when considering all operations at once.

First, let's determine the capitalization of the final string.
This can be done fairly easily by the following criteria:

- Characters positioned at places where the depth of the bracket sequence is **even** will not change their capitalization.
- Characters positioned at places where the depth of the bracket sequence is **odd** will change their capitalization.

By rearranging the characters accordingly based on this criteria, we no longer need to consider changing the capitalization of characters.

Now, let's focus on the following operations:

- For contiguous substrings where the first and last characters are `(` and `)` respectively, remove the `(` and `)` and reverse the substring.

The final string can be obtained through the following recursive process:

- Define a recursive function $f(l, r, d)$.
- When $d = 0$, examine characters from $l$ to $r$ sequentially. Output each character encountered.
  - If a `(` is found at position $l_u$ during this process, find the corresponding `)` at position $r_u$.
  - Call $f(l_u + 1, r_u - 1, 1)$, then continue processing from position $r_u + 1$. (Note that characters after position $r_u$ will be output after the processing from position $l_u$ to $r_u$ is completed.)
- When $d = 1$, examine characters from $r$ to $l$ sequentially. Output each character encountered.
  - If a `)` is found at position $r_u$ during this process, find the corresponding `(` at position $l_u$.
  - Call $f(l_u + 1, r_u - 1, 0)$, then continue processing from position $l_u-1$.

The corresponding `(` and `)` can be precomputed with a time complexity of $O(|S|)$.
Then, calling $f(1,|S|,0)$ allows solving this problem with a time complexity of $O(|S|)$.

#### Implementation (C++):

<details><summary>C++ </summary>

```cpp
#include<bits/stdc++.h>

using namespace std;

char flp(char c){
  if('A'<=c && c<='Z'){
    return (c-'A'+'a');
  }
  return (c-'a'+'A');
}

string s;
vector<int> mch;

void f(int l,int r,int d){
  if(d==0){
    while(l<=r){
      if(s[l]=='('){
        f(l+1,mch[l]-1,1);
        l=mch[l];
      }
      else{
        cout << s[l];
      }
      l++;
    }
  }
  else{
    while(l<=r){
      if(s[r]==')'){
        f(mch[r]+1,r-1,0);
        r=mch[r];
      }
      else{
        cout << s[r];
      }
      r--;
    }
  }
}

int main(){
  cin >> s;
  int l=s.size();
  mch.resize(l);
  for(auto &nx : mch){nx=-1;}

  int h=0;
  vector<int> stk;
  for(int i=0;i<l;i++){
    if(s[i]=='('){
      stk.push_back(i);
      h++;
    }
    else if(s[i]==')'){
      mch[i]=stk.back();
      mch[stk.back()]=i;
      stk.pop_back();
      h--;
    }
    else if(h%2){
      s[i]=flp(s[i]);
    }
  }

  f(0,l-1,0);
  return 0;
}
```

</details>


> [Comment](https://codeforces.com/blog/entry/128633?#comment-1142032) [1](https://atcoder.jp/contests/abc350/submissions/52597806)