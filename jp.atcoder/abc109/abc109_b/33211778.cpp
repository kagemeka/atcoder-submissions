#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<string> w(n);
  for(int i = 0; i < n; i++) cin >> w[i];
  bool ok = true;
  for(int i = 0; i < n - 1; i++) {
    if(w[i][w[i].size() - 1] != w[i + 1][0]) ok = false;
  }
  sort(w.begin(), w.end());
  for(int i = 0; i < n - 1; i++) {
    if(w[i] == w[i + 1]) ok = false;
  }
  cout << (ok ? "Yes" : "No") << endl;
}
