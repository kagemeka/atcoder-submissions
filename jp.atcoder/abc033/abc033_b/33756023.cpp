#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  string t;
  int mx = 0;
  long tot = 0;
  for(int i = 0; i < n; i++) {
    string s;
    int p;
    cin >> s >> p;
    tot += p;
    if(p > mx) {
      mx = p;
      t = s;
    }
  }
  cout << (mx * 2 > tot ? t : "atcoder") << endl;
}
