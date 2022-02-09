#include <bits/stdc++.h>


int main() {
  using namespace std;

  int n = 1 << 20;
  int q;
  cin >> q;
  set<int> idx;
  for (int i = 0; i < n; i++) {
    idx.insert(i);
  }
  vector<long long> a(n, -1);
  while (q--) {
    int t;
    long long x;
    cin >> t >> x;
    if (t == 1) {
      int i = *idx.lower_bound(x % n);
      if (i == (int)idx.size()) {
        i = 0;
      }
      a[i] = x;
      idx.erase(i);
      // cout << x % n << ' ' << i << endl;
    } else {
      cout << a[x % n] << endl;
    }
  }
}
