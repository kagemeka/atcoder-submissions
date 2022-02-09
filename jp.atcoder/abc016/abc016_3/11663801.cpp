#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m;
  cin >> n >> m;
  vector<unordered_set<int>> friends(n);
  for (int i = 0; i < m; i++) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    friends[a].insert(b);
    friends[b].insert(a);
  }
  for (int i = 0; i < n; i++) {
    unordered_set<int> res;
    for (auto &j : friends[i]) {
      for (auto &k : friends[j]) res.insert(k);
    }
    for (auto &j : friends[i]) res.erase(j);
    res.erase(i);
    cout << res.size() << '\n';

  }
  return 0;
}
