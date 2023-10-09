#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  vector<int> cases(n + 1), cd(n + 1);
  for(int i = 0; i < n + 1; i++) {
    cases[i] = i;
    cd[i] = i;
  }
  int x = 0;
  while(m--) {
    int y;
    cin >> y;
    swap(cd[cases[x]], cd[cases[y]]);
    swap(cases[x], cases[y]);
    swap(x, y);
  }
  for(int i = 0; i < n; i++) { cout << cd[i + 1] << " \n"[i == n - 1]; }
}
