#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) {
    cin >> a[i];
    a[i]--;
  }
  for(int i = 0; i < n; i++) {
    int x = i;
    for(int j = 0; j < n; j++) {
      x = a[x];
      if(x == i) {
        cout << j + 1 << endl;
        break;
      }
    }
  }
}
