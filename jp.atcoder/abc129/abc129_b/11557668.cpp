#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<int> w(n);
  for (int i = 0; i < n; i++) {
    cin >> w[i];
  }
  for (int i = 0; i < n - 1; i++) {
    w[i+1] += w[i];
  }
  int s = w[n-1];
  int res = s;
  for (int i = 0; i < n; i++) {
    res = min(res, abs(s - 2 * w[i]));
  }
  cout << res << '\n';
  return 0;
}
