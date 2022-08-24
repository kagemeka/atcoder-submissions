#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  vector<int> s(n);
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < 3; j++) {
      int p;
      cin >> p;
      s[i] += p;
    }
  }
  auto a = s;
  sort(s.rbegin(), s.rend());
  int v = s[k - 1] - 300;
  for(auto& x: a) { cout << (x >= v ? "Yes" : "No") << endl; }
}
