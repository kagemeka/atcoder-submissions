#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  int const k = 1 << 18;
  vector<int> cnt(k);
  long s = 0;
  for(int i = 0; i < n; i++) {
    int x;
    cin >> x;
    cnt[x]++;
    s += x;
  }
  int q;
  cin >> q;
  while(q--) {
    int x, y;
    cin >> x >> y;
    int c = cnt[x];
    s += (long)(y - x) * c;
    cnt[y] += c;
    cnt[x] = 0;
    cout << s << '\n';
  }
}
