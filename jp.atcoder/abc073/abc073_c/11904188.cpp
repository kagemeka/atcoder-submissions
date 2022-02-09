#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  bitset<1001001001> res(0);
  int n; cin >> n;
  for (int i = 0; i < n; i++) {
    int a; cin >> a;
    res.flip(a);
  }
  cout << res.count() << '\n';
  return 0;
}
