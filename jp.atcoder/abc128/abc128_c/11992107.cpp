#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, m; cin >> n >> m;
  vector<vector<int>> graph(n);
  for (int i = 0; i < m; i++) {
    int k; cin >> k;
    for (int j = 0; j < k; j++) {
      int s; cin >> s;
      s--;
      graph[s].push_back(i);
    }
  }
  vector<int> p(m);
  for (int i = 0; i < m; i++) cin >> p[i];
  int cnt = 0;
  for (int i = 0; i < (1 << n); i++) {
    bitset<10> light(0);
    for (int j = 0; j < n; j++) {
      if (i >> j & 1) {
        for (int s : graph[j]) {
          light.flip(s);
        }
      }
    }
    bool flag = true;
    for (int j = 0; j < m; j++) {
      if (light[j] ^ p[j]) {
        flag = false;
        break;
      }
    }
    if (flag) cnt++;
  }
  cout << cnt << '\n';
  return 0;
}
