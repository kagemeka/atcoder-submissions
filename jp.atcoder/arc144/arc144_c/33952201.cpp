#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  if(k > n / 2) {
    cout << -1 << endl;
    return 0;
  }
  vector<int> a(n);
  iota(a.begin(), a.end(), 1);
  vector<int> state(n);
  int i = 0;
  while(true) {
    if(state[i] == 1) {
      i++;
      continue;
    }
    if(i + k >= n) break;
    swap(a[i], a[i + k]);
    state[i] = -1;
    state[i + k] = 1;
    i++;
  }
  int l = i;
  while(i < n && state[i] == 0) {
    swap(a[i - k], a[i]);
    state[i] = 1;
    state[i - k] = -1;
    i++;
  }
  int r = i;
  while(l > 1 && state[l - 1] == 1) l--;
  sort(a.begin() + l, a.begin() + r);
  for(int i = 0; i < n; i++) cout << a[i] << " \n"[i == n - 1];
}
