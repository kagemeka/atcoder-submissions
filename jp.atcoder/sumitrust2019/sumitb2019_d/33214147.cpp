#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  string s;
  cin >> n >> s;
  vector<vector<int>> pos(10);
  for(int i = 0; i < n; i++) { pos[s[i] - '0'].push_back(i); }
  auto is_ok = [&](int i) -> bool {
    vector<int> d;
    d.push_back(i % 10);
    i /= 10;
    d.push_back(i % 10);
    d.push_back(i / 10);
    i = -1;
    while(d.size()) {
      int x = d.back();
      d.pop_back();
      auto ptr = lower_bound(pos[x].begin(), pos[x].end(), i + 1);
      if(ptr == pos[x].end()) return false;
      i = *ptr;
    }
    return true;
  };
  int cnt = 0;
  for(int i = 0; i < 1000; i++) cnt += is_ok(i);
  cout << cnt << endl;
}
