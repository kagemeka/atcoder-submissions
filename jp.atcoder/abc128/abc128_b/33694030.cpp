#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<string> s(n);
  vector<int> p(n);
  for(int i = 0; i < n; i++) cin >> s[i] >> p[i];
  vector<int> idx(n);
  iota(idx.begin(), idx.end(), 0);
  sort(idx.begin(), idx.end(), [&](int i, int j) -> bool {
    if(s[i] != s[j]) return s[i] < s[j];
    return p[i] > p[j];
  });
  for(auto& i: idx) { cout << i + 1 << endl; }
}
