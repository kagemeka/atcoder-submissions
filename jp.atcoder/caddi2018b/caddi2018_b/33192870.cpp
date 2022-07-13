#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  int v = 0;
  while(n--) {
    int x;
    cin >> x;
    v |= x & 1;
  }
  cout << (v ? "first" : "second") << endl;
}
