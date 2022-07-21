#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int x, y, a, b, c;
  cin >> x >> y >> a >> b >> c;
  using pi = pair<int, int>;
  vector<pi> items;
  for(int i = 0; i < a; i++) {
    int v;
    cin >> v;
    items.emplace_back(v, 0);
  }
  for(int i = 0; i < b; i++) {
    int v;
    cin >> v;
    items.emplace_back(v, 1);
  }
  for(int i = 0; i < c; i++) {
    int v;
    cin >> v;
    items.emplace_back(v, 2);
  }
  sort(items.rbegin(), items.rend());
  long s = 0;
  int r = 0;
  for(auto& [v, j]: items) {
    if(j == 0 && x > 0) {
      x--;
      s += v;
    }
    if(j == 1 && y > 0) {
      y--;
      s += v;
    }
    if(j == 2) {
      s += v;
      r++;
    }
    if(x + y == r) { break; }
  }
  cout << s << endl;
}
