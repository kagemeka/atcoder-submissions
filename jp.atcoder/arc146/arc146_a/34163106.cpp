#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  sort(a.rbegin(), a.rend());
  string s = "";
  for(int i = 0; i < 3; i++) { s += to_string(a[i]); }
  cout << s << endl;
}
