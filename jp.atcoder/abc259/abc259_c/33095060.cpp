#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  string s;
  string t;
  cin >> s >> t;
  auto encode = [&](string s) -> vector<int> {
    int n = s.size();
    char prev = '$';
    int cnt = 0;
    vector<int> res;
    for(int i = 0; i < n; i++) {
      if(s[i] == prev) {
        cnt++;
        prev = s[i];
        continue;
      }
      prev = s[i];
      res.push_back(cnt);
      cnt = 1;
    }
    res.push_back(cnt);
    return res;
  };
  auto a = encode(s);
  auto b = encode(t);
  int n = a.size();
  int m = b.size();
  // cout << n << m << endl;
  if(n != m) {
    cout << "No" << endl;
    return 0;
  }
  for(int i = 0; i < n; i++) {
    if(a[i] == b[i]) continue;
    if(a[i] > b[i] || a[i] == 1) {
      cout << "No" << endl;
      return 0;
    }
  }
  cout << "Yes" << endl;
}
