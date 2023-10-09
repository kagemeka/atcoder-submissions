#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  int const k = 10;
  int s = (1 << k) - 1;
  int lo = 0;
  for(int i = 0; i < m; i++) {
    int x;
    cin >> x;
    s &= ~(1 << x);
    if(x == lo) lo++;
  }
  vector<int> next(k);
  int x = -1;
  for(int i = k - 1; i >= 0; i--) {
    next[i] = x;
    if(s >> i & 1) x = i;
  }
  int p = 1;
  x = 0;
  int mn = 0;
  bool just = true;
  while(n) {
    int d = n % k;
    n /= k;
    mn = mn * k + lo;
    if(just && s >> d & 1) {
      x += p * d;
      p *= k;
      continue;
    }
    d = next[d];
    if(d == -1) {
      x = mn;
      just = false;
    } else {
      x = mn / k + p * d;
      just = true;
    }
    p *= k;
  }
  if(!just) x += next[0] * p;
  cout << x << endl;
}
