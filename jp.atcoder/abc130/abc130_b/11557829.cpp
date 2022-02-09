#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, x;
  cin >> n >> x;
  vector<int> d(n+1);
  int ans = n + 1;
  bool flag = false;
  for (int i = 0; i < n; i++) {
    int l;
    cin >> l;
    d[i+1] = d[i] + l;
    if (!flag && d[i+1] > x) {
      ans = i + 1;
      flag = true;
    }
  }
  cout << ans << '\n';
  return 0;
}
