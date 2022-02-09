#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m, c;
  cin >> n >> m >> c;
  vector<int> b(m);
  for (int i = 0; i < m; i++) {
    cin >> b[i];
  }
  int a;
  int cnt = 0;
  for (int i = 0; i < n; i++) {
    int s = c;
    for (int j = 0; j < m; j++) {
      cin >> a;
      s += a * b[j];
    }
    cnt += s > 0;
  }
  cout << cnt << '\n';
  return 0;
}
