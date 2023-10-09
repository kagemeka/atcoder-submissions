#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  string s;
  cin >> n >> s;

  int cnt_r = 0;
  for(auto& c: s) cnt_r += c == 'R';
  int res = 0;
  for(int i = 0; i < cnt_r; i++) { res += s[i] == 'W'; }
  cout << res << endl;
}
