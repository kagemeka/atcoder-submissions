#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<int> deg(n);
  while(m--) {
    int a, b;
    cin >> a >> b;
    a--;
    b--;
    deg[a]++;
    deg[b]++;
  }
  for(int d: deg) cout << d << endl;
}
