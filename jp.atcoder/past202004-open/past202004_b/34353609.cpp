#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  cin >> s;
  vector<int> cnt(3);
  for(auto& c: s) cnt[c - 'a']++;
  int res = -1;
  int c = -1;
  for(int i = 0; i < 3; i++) {
    if(cnt[i] > c) {
      c = cnt[i];
      res = i;
    }
  }
  cout << (char)(res + 'a') << endl;
}
