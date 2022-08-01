#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int const k = 1 << 20;
  vector<int> c(k);
  for(auto& x: a) c[x]++;
  bool ok = true;
  for(int i = 2; i < k; i++) {
    int x = 0;
    for(int j = i; j < k; j += i) { x += c[j]; }
    if(x > 1) ok = false;
  }
  if(ok) {
    cout << "pairwise coprime" << endl;
    return 0;
  }
  int g = 0;
  for(auto& x: a) g = gcd(g, x);
  if(g == 1) {
    cout << "setwise coprime" << endl;
  } else {
    cout << "not coprime" << endl;
  }
}
