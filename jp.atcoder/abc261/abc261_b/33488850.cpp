#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<string> s(n);
  for(int i = 0; i < n; i++) cin >> s[i];
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < i; j++) {
      if(s[i][j] == 'W') {
        s[i][j] = 'L';
      } else if(s[i][j] == 'L') {
        s[i][j] = 'W';
      }
    }
  }
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < i; j++) {
      if(s[i][j] == s[j][i]) continue;
      cout << "incorrect" << endl;
      return 0;
    }
  }
  cout << "correct" << endl;
}
