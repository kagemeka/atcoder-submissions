#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  int n2 = 1 << n;
  if(k >= n2 || (n == 1 && k == 1)) {
    cout << -1 << endl;
    return 0;
  }
  if(n == 0) {
    cout << 0 << ' ' << 0 << endl;
    return 0;
  }
  if(n == 1) {
    vector<int> res = {0, 0, 1, 1};
    for(int i = 0; i < 4; i++) { cout << res[i] << " \n"[i == 3]; }
    return 0;
  }
  vector<int> res(n2 << 1);
  int i = 0;
  for(int j = 0; j < n2; j++) {
    if(j == k) continue;
    res[i] = j;
    i++;
  }
  res[i] = k;
  i++;
  for(int j = n2; j-- > 0;) {
    if(j == k) continue;
    res[i] = j;
    i++;
  }
  res[i] = k;
  for(int i = 0; i < n2 << 1; i++) {
    cout << res[i] << " \n"[i == (n2 << 1) - 1];
  }
}
