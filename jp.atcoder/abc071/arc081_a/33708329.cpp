#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  map<int, int> cnt;
  for(int i = 0; i < n; i++) {
    int x;
    cin >> x;
    cnt[-x]++;
  }
  int h = 0, w = 0;
  for(auto& [x, c]: cnt) {
    if(h == 0 && c >= 2) {
      c -= 2;
      h = -x;
    }
    if(w == 0 && c >= 2) {
      c -= 2;
      w = -x;
    }
  }
  cout << (long)h * w << endl;
}
