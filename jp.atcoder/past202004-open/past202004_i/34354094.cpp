#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(1 << n);
  for(int i = 0; i < 1 << n; i++) {
    cin >> a[i];
    a[i]--;
  }
  vector<int> res(1 << n);
  vector<int> que(1 << n);
  iota(que.begin(), que.end(), 0);
  int d = 1 << n;
  int i = 0;
  int r = 0;
  while(d > 1) {
    r++;
    int t = i + d;
    while(i < t) {
      int j = que[i];
      int k = que[i + 1];
      if(a[j] > a[k]) {
        que.push_back(j);
        res[k] = r;
      } else {
        que.push_back(k);
        res[j] = r;
      }
      i += 2;
    }
    assert(i == t);
    d >>= 1;
  }
  res[que[i]] = r;
  for(auto& r: res) cout << r << '\n';
}
