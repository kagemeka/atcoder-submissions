#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  string res = string(n, '0');
  if(n > 1) { res[0] = '1'; }
  int fixed = 0;
  int ok = true;
  while(m--) {
    int i;
    char d;
    cin >> i >> d;
    i--;
    if(fixed >> i & 1 && res[i] != d) {
      ok = false;
      continue;
    }
    if(n > 1 && i == 0 && d == '0') {
      ok = false;
      continue;
    }
    fixed |= 1 << i;
    res[i] = d;
  }
  if(ok) {
    cout << res;
  } else {
    cout << -1;
  }
  cout << endl;
}
