#include <bits/stdc++.h>
using namespace std;


void solve() {
  int n = 4;
  vector<char> c(n*n);
  for (int i = 0; i < n*n; i++)
  {
    cin >> c[i];
  }
  reverse(c.begin(), c.end());
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++)
    {
      cout << c[n*i + j];
      if (j == n - 1) continue;
      cout << ' ';
    }
    cout << '\n';
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
