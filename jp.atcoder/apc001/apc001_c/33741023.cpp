#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  map<string, int> idx;
  idx["Male"] = 0;
  idx["Female"] = 1;
  idx["Vacant"] = -1;
  auto query = [&](int i) -> int {
    cout << i << endl;
    string s;
    cin >> s;
    return idx[s];
  };
  int x = query(0);
  if(x == -1) { return 0; }
  int x0 = x;
  auto f = [&](int i) -> int {
    int x = query(i);
    if(x == -1) return -1;
    return x0 ^ x;
  };
  int lo = 1, hi = n;
  while(hi - lo > 0) {
    int i = (lo + hi) >> 1;
    int p = i & 1;
    int x = f(i);
    if(x == -1) return 0;
    if(p ^ x) {
      hi = i;
    } else {
      lo = i + 1;
    }
  }
}
