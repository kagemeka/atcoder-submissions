#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, l;
  cin >> n >> l;
  vector<string> s(n);
  for(int i = 0; i < n; i++) cin >> s[i];
  sort(s.begin(), s.end());
  string t = "";
  for(int i = 0; i < n; i++) t += s[i];
  cout << t << endl;
}
