#include <bits/stdc++.h>
using namespace std;


void solve() {
  int n, k;
  cin >> n >> k;
  vector<int> r(n);
  for (int i = 0; i < n; i++) {
    cin >> r[i];
  }
  sort(
    r.begin(),
    r.end(),
    greater<int>()
  );
  double rate = 0;
  for (int i = k-1; i > -1; i--)
  {
    rate = (rate + r[i]) / 2;
  }
  cout << setprecision(10)
    << rate << '\n';
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
