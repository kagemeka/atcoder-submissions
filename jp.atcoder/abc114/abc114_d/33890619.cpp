#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> cnt(n + 1);
  for(int i = 1; i <= n; i++) {
    int x = i;
    for(int i = 2; i * i <= x; i++) {
      while(x % i == 0) {
        cnt[i]++;
        x /= i;
      }
    }
    if(x > 1) cnt[x]++;
  }
  vector<int> c(100);
  for(auto& x: cnt) { c[x]++; }
  for(int i = 100; i-- > 1;) { c[i - 1] += c[i]; }
  vector<vector<int>> cand = {
    {75                       },
    { 25, 3},
    { 15,  5},
    { 5,                         5, 3},
  };
  int s = 0;
  for(auto& b: cand) {
    int p = 1;
    int m = b.size();
    for(int i = 0; i < m; i++) { p *= c[b[i] - 1] - i; }
    if(b[0] == 5) p /= 2;
    s += p;
  }
  cout << s << endl;
}
