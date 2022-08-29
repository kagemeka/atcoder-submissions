#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  cin >> s;
  string t = "AZ";
  for(int i = 0; i < 2; i++) {
    reverse(s.begin(), s.end());
    char c = t[i];
    while(s.back() != c) s.pop_back();
  }
  cout << s.size() << endl;
}
