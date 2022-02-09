#include <bits/stdc++.h>
using namespace std;


void solve() {
  int n = 4;
  vector<string> c(n);
  for (int i = 0; i < n; i++) {
    getline(cin, c[i]);
    reverse(
      c[i].begin(),
      c[i].end()
    );
  }
  reverse(c.begin(), c.end());
  for (int i = 0; i < n; i++) {
    cout << c[i] << '\n';
  }
}


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int t = 1;
  while (t--) {
    solve();
  }

  return 0;
}
