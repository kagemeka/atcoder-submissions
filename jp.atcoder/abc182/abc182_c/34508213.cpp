#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  cin >> s;
  int n = s.size();
  vector<int> cnt(3);
  int v = 0;
  for(auto& c: s) {
    int d = (c - '0') % 3;
    cnt[d]++;
    v += d;
  }
  v %= 3;
  if(v == 0) {
    cout << 0 << endl;
  } else if(cnt[v] && n > 1) {
    cout << 1 << endl;
  } else if(cnt[v ^ 3] >= 2 && n > 2) {
    cout << 2 << endl;
  } else {
    cout << -1 << endl;
  }
}
