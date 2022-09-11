#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  int n2 = n * 2;
  vector<int> a(n2);
  for(int i = 0; i < n2; i++) cin >> a[i];
  map<int, int> c;
  for(auto& x: a) c[x]++;
  for(auto& [x, c]: c) {
    // cout << c << endl;
    if(c & 1) {
      cout << "Alice" << endl;
      return 0;
    }
  }
  cout << "Bob" << endl;
}
