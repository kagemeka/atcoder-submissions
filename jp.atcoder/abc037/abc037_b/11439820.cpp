#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, q;
  cin >> n >> q;
  vector<int> a(n);

  int l, r, t;
  for (int i = 0; i < q; i++) {
    cin >> l >> r >> t;
    for (int j = l-1; j < r; j++) a[j] = t;
  }
  for (int &v : a) {cout << v << '\n';}
  return 0;
}
