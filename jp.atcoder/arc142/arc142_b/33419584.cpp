#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j += 2) {
      int x = i * n + j + 1;
      int y = i * n + j + 2;
      if(j != n - 1) {
        cout << y << ' ' << x;
        if(j < n - 2) cout << ' ';
      } else {
        cout << x;
      }
    }
    cout << endl;
  }
}
