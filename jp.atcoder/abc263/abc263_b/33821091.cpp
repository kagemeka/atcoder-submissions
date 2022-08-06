#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> p(n, -1);
  for(int i = 0; i < n - 1; i++) {
    cin >> p[i + 1];
    p[i + 1]--;
  }
  int d = 0;
  int u = n - 1;
  while(u != 0) {
    d++;
    u = p[u];
  }
  cout << d << endl;
}
