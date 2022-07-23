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
        if(i & 1) swap(x, y);
        cout << x << ' ' << y << ' ';
      } else {
        cout << x;
      }
    }
    cout << endl;
  }
}
