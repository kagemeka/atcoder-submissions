#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, a, b, k;
  cin >> n >> a >> b >> k;

  unordered_set<int> visited;
  visited.insert(a);
  visited.insert(b);

  int p;
  for (int i = 0; i < k; i++) {
    cin >> p;
    visited.insert(p);
  }
  string ans = (visited.size() == k + 2) ? "YES" : "NO";
  cout << ans << '\n';
  return 0;
}
