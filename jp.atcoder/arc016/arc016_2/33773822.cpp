#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int h;
  cin >> h;
  int const w = 9;
  vector<string> s(h);
  for(int i = 0; i < h; i++) cin >> s[i];
  int cnt = 0;
  for(int i = 0; i < h; i++) {
    for(int j = 0; j < w; j++) {
      if(s[i][j] == 'x') cnt++;
      if(s[i][j] == 'o' && (i == 0 || s[i - 1][j] != 'o')) cnt++;
    }
  }
  cout << cnt << endl;
}
