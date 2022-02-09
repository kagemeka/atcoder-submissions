#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, m; cin >> n >> m;
  vector<int> a(n);
  bitset<10> confirmed(0);

  for (int i = 0; i < m; i++) {
    int s, c; cin >> s >> c; s--;
    if (confirmed[s] && a[s] != c) {
      cout << -1 << '\n';
      return 0;
    } else if (s == 0 && c == 0){
      cout << -1 << '\n';
      return 0;
    } else {
      a[s] = c;
      confirmed.set(s);
    }
  }
  if (!confirmed[0] && n > 1) a[0] = 1;
  string res = "";
  for (auto &d : a) {
    res += to_string(d);
  }
  cout << res << '\n';
  return 0;
}
