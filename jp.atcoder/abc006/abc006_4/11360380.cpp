#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> c(n);
  for (int i = 0; i < n; i++) {
    cin >> c[i];
  }

  int INF = 100100;
  vector<int> res(n, INF);
  for (int x : c) {
    int i = lower_bound(res.begin(), res.end(), x) - res.begin();
    res[i] = x;
  }

  int ans = n - (lower_bound(res.begin(), res.end(), INF) - res.begin());
  cout << ans << endl;
  return 0;
}
