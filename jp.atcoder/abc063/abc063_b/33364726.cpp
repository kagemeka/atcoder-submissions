#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  cin >> s;
  sort(s.begin(), s.end());
  int n = s.size();
  for(int i = 0; i < n - 1; i++) {
    if(s[i] == s[i + 1]) {
      cout << "no" << endl;
      return 0;
    }
  }
  cout << "yes" << endl;
}
