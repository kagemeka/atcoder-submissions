#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  sort(a.rbegin(), a.rend());
  vector<string> b;
  for(int i = 0; i < 3; i++) b.push_back(to_string(a[i]));
  sort(b.rbegin(), b.rend());
  string s = "";
  for(int i = 0; i < 3; i++) { s += b[i]; }
  cout << s << endl;
}
