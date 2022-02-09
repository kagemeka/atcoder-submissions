#include <bits/stdc++.h>
using namespace std;

using ull = unsigned long long;


template<typename T>
int bit_cnt(T n) {
  int c = 0;
  for (; n > 0; n >>= 1) {
    c += n & 1;
  }
  return c;
}


class Solve {
  int n, k;
  vector<int> a;
  set<ull> searched;


  void prepare() {
    cin >> n >> k;
    for (
      int i = 0; i < n * n; i++
    ) {
      char c; cin >> c;
      a.push_back(c - '#');
    }
  }


  vector<int> adjacent(int i) {
    vector<int> b;
    int y = i / n, x = i % n;
    if (y > 0) {
      b.push_back(i - n);
    }
    if (y < n - 1) {
      b.push_back(i + n);
    }
    if (x > 0) {
      b.push_back(i - 1);
    }
    if (x < n - 1) {
      b.push_back(i + 1);
    }
    return b;
  }


  int dfs(ull s) {
    if (searched.count(s)) {
      return 0;
    }
    searched.insert(s);
    if (bit_cnt(s) == k) {
      return 1;
    }
    int tot = 0;
    for (
      int i = 0; i < n * n; i++
    ) {
      if (~s >> i & 1) {
        continue;
      }
      for (int j: adjacent(i))
      {
        if (s >> j & 1) {
          continue;
        }
        if (!a[j]) continue;
        ull ns = s | 1ull << j;
        tot += dfs(ns);
        searched.insert(ns);
      }
    }
    return tot;
  }


public:
  void operator()() {
    prepare();
    int tot = 0;
    for (
      int i = 0; i < n * n; i++
    ) {
      if (!a[i]) continue;;
      tot += dfs(1ull << i);
    }
    cout << tot << '\n';
  }
};


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  Solve()();
  return 0;
}
