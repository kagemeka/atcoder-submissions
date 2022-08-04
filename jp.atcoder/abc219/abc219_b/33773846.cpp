#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  vector<string> s(3);
  for(int i = 0; i < 3; i++) cin >> s[i];
  string t;
  cin >> t;
  string w = "";
  for(auto& c: t) {
    int d = c - '1';
    w += s[d];
  }
  cout << w << endl;
}
