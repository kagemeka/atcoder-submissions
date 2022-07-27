#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  map<int, int> cnt;
  for(int i = 0; i < n; i++) {
    int x;
    cin >> x;
    cnt[x]++;
  }
  int res = 0;
  for(auto& [x, c]: cnt) {
    if(c < x) res += c;
    else res += c - x;
  }
  cout << res << endl;
}
