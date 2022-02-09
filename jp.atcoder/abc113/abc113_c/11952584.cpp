#include <bits/stdc++.h>
using namespace std;

string fill(string s) {
  while (s.size() < 6) s = "0" + s;
  return s;
}

string create_id(int p, int o) {
  return fill(to_string(p)) + fill(to_string(o));
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m; cin >> n >> m;
  vector<int> p(m);
  vector<int> y(m);
  for (int i = 0; i < m; i++) cin >> p[i] >> y[i];
  vector<vector<vector<int>>> db(n + 1);
  for (int i = 0; i < m; i++) {
    db[p[i]].push_back({y[i], i});
  }
  vector<string> res(m);
  for (int i = 1; i < n + 1; i++) {
    sort(db[i].begin(), db[i].end());
    for (int j = 0; j < db[i].size(); j++) {
      res[db[i][j][1]] = create_id(i, j + 1);
    }
  }
  for (string &id : res) {
    cout << id << '\n';
  }
  return 0;
}
