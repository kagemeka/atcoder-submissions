#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  double n; cin >> n;
  vector<int> x(n);
  for (int i = 0; i < n; i++) cin >> x[i];
  int p = round(accumulate(x.begin(), x.end(), 0) / n);
  int res = 0;
  for (auto &i : x) {
    res += pow(p - i, 2);
  }
  cout << res << '\n';
  return 0;
}
