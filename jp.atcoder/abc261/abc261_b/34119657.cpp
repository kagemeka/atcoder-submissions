#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<string> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < i; j++) {
      bool ok = true;
      if(a[i][j] == 'D' && a[j][i] != 'D') ok = false;
      if(a[i][j] == 'W' && a[j][i] != 'L') ok = false;
      if(a[i][j] == 'L' && a[j][i] != 'W') ok = false;
      if(!ok) {
        cout << "incorrect" << endl;
        return 0;
      }
    }
  }
  cout << "correct" << endl;
}
