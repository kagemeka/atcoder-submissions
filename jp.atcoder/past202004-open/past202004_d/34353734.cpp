#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  cin >> s;
  string pool = ".";
  for(char c = 'a'; c <= 'z'; c++) { pool += c; }
  vector<string> a{""};
  for(int i = 0; i < (int)a.size(); i++) {
    string t = a[i];
    if(t.size() == 3) break;
    for(auto& c: pool) { a.push_back(t + c); }
  }
  auto f = [&](string t) -> bool {
    int n = s.size();
    int m = t.size();
    if(m > n) return false;
    for(int i = 0; i < n - m + 1; i++) {
      bool flg = true;
      for(int j = 0; j < m; j++) {
        if(t[j] == '.') continue;
        if(s[i + j] == t[j]) continue;
        flg = false;
      }
      if(flg) return true;
    }
    return false;
  };
  int cnt = 0;
  for(int i = 1; i < (int)a.size(); i++) { cnt += f(a[i]); }
  cout << cnt << '\n';
}
