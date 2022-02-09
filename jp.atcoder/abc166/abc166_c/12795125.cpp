#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, m; cin >> n >> m;
  vector<int> h(n);
  for (int i = 0; i < n; i++) {
    cin >> h[i];
  }
  vector<vector<int>> surround(n, vector<int>(0));
  for (int i = 0; i < m; i++) {
    int a, b; cin >> a >> b; a--; b--;
    surround[a].push_back(h[b]);
    surround[b].push_back(h[a]);
  }
  int tot = 0;
  for (int i = 0; i < n; i++) {
    if (surround[i].empty()) {
      tot++;
    } else if (h[i] > *max_element(surround[i].begin(), surround[i].end())) {
      tot++;
    }
  }
  cout << tot << '\n';
  return 0;
}
