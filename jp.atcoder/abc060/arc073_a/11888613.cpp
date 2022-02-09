#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, T;
  cin >> n >> T;
  vector<int> t(n);
  for (int i = 0; i < n; i++) cin >> t[i];
  int pushed = t[0];
  int tot = 0;
  for (int i = 1; i < n; i++) {
    tot += min(T, t[i] - pushed);
    pushed = t[i];
  }
  tot += T;
  cout << tot << '\n';
  return 0;
}
