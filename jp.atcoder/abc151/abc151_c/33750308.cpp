#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<bool> accepted(n);
  vector<int> cnt(n);
  int ac = 0;
  int pe = 0;
  for(int i = 0; i < m; i++) {
    int p;
    string s;
    cin >> p >> s;
    p--;
    if(s == "WA") {
      cnt[p]++;
      continue;
    }
    if(accepted[p]) { continue; }
    accepted[p] = true;
    ac++;
    pe += cnt[p];
  }
  cout << ac << ' ' << pe << endl;
}
