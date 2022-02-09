#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> p(n);
  for (int i = 0; i < n; i++) cin >> p[i];
  int m = 1001001001;
  int cnt = 0;
  for (int i = 0; i < n; i++) {
    if (m < p[i]) continue;
    cnt++;
    m = p[i];
  }
  cout << cnt << '\n';
  return 0;
}
