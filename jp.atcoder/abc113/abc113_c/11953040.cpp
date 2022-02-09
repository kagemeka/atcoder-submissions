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
  vector<vector<int>> db(m, vector<int>(3));
  for (int i = 0; i < m; i++) {
    cin >> db[i][0] >> db[i][1];
    db[i][2] = i;
  }
  sort(db.begin(), db.end());
  vector<string> res(m);
  int prev = 0, j;
  for (auto &t : db) {
    (t[0] == prev) ? j++ : j = 1;
    res[t[2]] = create_id(t[0], j);
    prev = t[0];
  }
  for (string &id : res) {
    cout << id << '\n';
  }
  return 0;
}
