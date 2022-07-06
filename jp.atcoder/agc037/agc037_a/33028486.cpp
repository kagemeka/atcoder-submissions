#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  string s;
  cin >> s;
  int n = s.size();

  int k = 0;
  bool tmp_flg = false;
  for(int i = 0; i < n; i++) {
    if(i >= 1 && s[i] != s[i - 1]) {
      k++;
      tmp_flg = false;
      continue;
    }
    if(i == 0 || tmp_flg) {
      k++;
      tmp_flg = false;
    } else {
      tmp_flg = true;
    }
  }
  k += tmp_flg;
  cout << k << endl;
}