#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> w(n), dist(n);
  for(int i = 0; i < n; i++) cin >> w[i];
  for(int i = 0; i < n; i++) cin >> dist[i];
  for(int i = 0; i < 2 * n; i++) {
    int j = i % n;
    int k = (i + 1) % n;
    dist[k] = min(dist[k], dist[j] + w[j]);
  }
  for(auto& d: dist) cout << d << endl;
}
