#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  string s;
  cin >> n >> s;
  vector<int> l{0}, r;
  for(int i = 0; i < n; i++) {
    if(s[i] == 'L') {
      r.push_back(l.back());
      l.pop_back();
    }
    l.push_back(i + 1);
  }
  while(r.size()) {
    l.push_back(r.back());
    r.pop_back();
  }
  for(int i = 0; i < n + 1; i++) { cout << l[i] << " \n"[i == n]; }
}
