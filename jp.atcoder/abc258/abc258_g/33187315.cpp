#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  int const k = 1 << 12;
  using bits = bitset<k>;
  vector<bits> a(n);
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      char x;
      cin >> x;
      if(x == '1') a[i].set(j);
    }
  }
  long tot = 0;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < i; j++) { tot += a[i][j] * (a[i] & a[j]).count(); }
  }
  cout << tot / 3 << endl;
}
