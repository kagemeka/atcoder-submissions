#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> r(n);
  for(int i = 0; i < n; i++) { cin >> r[i]; }
  vector<int> d(n);
  for(int i = 0; i < n - 1; i++) {
    if(r[i] < r[i + 1]) {
      d[i + 1] = 1;
    } else if(r[i] > r[i + 1]) {
      d[i + 1] = -1;
    } else {
      d[i + 1] = d[i];
    }
  }
  int c = 2;
  for(int i = 1; i < n - 1; i++) {
    if(d[i] * d[i + 1] == -1) { c++; }
  }
  cout << (c >= 3 ? c : 0) << endl;
}
