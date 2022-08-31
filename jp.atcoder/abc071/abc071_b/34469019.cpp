#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  cin >> s;
  vector<bool> f(26);
  for(auto& c: s) f[c - 'a'] = true;
  for(int i = 0; i < 26; i++) {
    if(f[i]) continue;
    cout << (char)(i + 'a') << endl;
    return 0;
  }
  cout << "None" << endl;
}
