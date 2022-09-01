#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  map<int, bool> p;
  for(int i = 0; i < n; i++) {
    int x;
    cin >> x;
    p[x] ^= true;
  }
  int cnt = 0;
  for(auto& [_, c]: p) { cnt += c; }
  cout << cnt << endl;
}
