#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  vector<string> s(n);
  for(int i = 0; i < n; i++) { cin >> s[i]; }
  vector<int> idx(n);
  iota(idx.begin(), idx.end(), 0);
  long used = 0;
  sort(idx.begin(), idx.end(), [&](int i, int j) -> bool {
    string a = s[i], b = s[j];
    return a + b < b + a;
  });
  string res = "";
  for(int i = 0; i < k - 1; i++) {
    res += s[idx[i]];
    used |= 1 << idx[i];
  }
  sort(idx.begin(), idx.end(), [&](int i, int j) -> bool {
    return s[i] < s[j];
  });
  for(int i = 0; i < n; i++) {
    int j = idx[i];
    if(used >> j & 1) continue;
    res += s[j];
    break;
  }
  cout << res << endl;
}
