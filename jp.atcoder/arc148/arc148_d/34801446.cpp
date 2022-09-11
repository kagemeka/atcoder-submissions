#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  int n2 = n * 2;
  vector<int> a(n2);
  for(int i = 0; i < n2; i++) cin >> a[i];
  // pair exist ?
  // alice: x, bob: y
  // y = x + km
  // \sum a = 2x + km;
  // 2x \equiv s (mod m)
  // sort(a.begin(), a.end());
  long s = 0;
  for(auto& x: a) {
    s += x;
    s %= m;
  }
  if(s & 1) {
    cout << "Alice" << endl;
    return 0;
  }
  s /= 2;
  map<int, int> c;
  for(auto& x: a) c[x]++;
  for(auto& [x, c]: c) {
    if(c & 1) {
      cout << "Alice" << endl;
      return 0;
    }
  }
  cout << "Bob" << endl;
}
