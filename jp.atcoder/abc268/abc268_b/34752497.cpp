#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s, t;
  cin >> s >> t;
  if(t.substr(0, s.size()) == s) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
}
