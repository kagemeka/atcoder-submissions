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
  vector<tuple<int, int, int>> db(m);
  for (int i = 0; i < m; i++) {
    int p, y; cin >> p >> y;
    db[i] = tuple<int, int, int>(p, y, i);
  }
  sort(db.begin(), db.end());
  vector<string> res(m);
  int prev = 0, j;
  for (auto &t : db) {
    int p = get<0>(t);
    int i = get<2>(t);
    (p == prev) ? j++ : j = 1;
    res[i] = create_id(p, j);
    prev = p;
  }
  for (string &id : res) {
    cout << id << '\n';
  }
  return 0;
}
