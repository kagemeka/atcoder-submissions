#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  string s;
  cin >> n >> s;
  int p_first = n;
  for(int i = 0; i < n; i++) {
    if(s[i] == 'd') continue;
    p_first = i;
    break;
  }
  auto f = [&](string s) -> string {
    string t = s;
    reverse(t.begin(), t.end());
    for(int i = 0; i < n; i++) t[i] = t[i] == 'p' ? 'd' : 'p';
    return t;
  };
  string now = s;
  for(int i = p_first; i < n; i++) {
    string x = s;
    string t = x.substr(p_first, i - p_first + 1);
    t = f(t);
    for(int j = p_first; j <= i; j++) { x[j] = t[j - p_first]; }
    now = min(now, x);
  }
  cout << now << endl;
}
