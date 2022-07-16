#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, k;
  cin >> n >> k;
  if(k > n / 2) {
    cout << -1 << endl;
    return 0;
  }
  vector<int> a(n);
  iota(a.begin(), a.end(), 1);
  vector<bool> from_left(n);
  vector<bool> swapped(n);
  int i = 0;
  while(i < n) {
    if(swapped[i]) {
      i++;
      continue;
    }
    if(i + k >= n) break;
    swap(a[i], a[i + k]);
    swapped[i] = true;
    swapped[i + k] = true;
    from_left[i + k] = true;
    i++;
  }
  int i0 = i;
  // cout << i << endl;
  // cout << swapped[i] << endl;
  while(i < n) {
    if(swapped[i]) break;
    swap(a[i], a[i - k]);
    swapped[i] = true;
    from_left[i] = true;
    from_left[i - k] = false;
    i++;
  }
  // cout << i << endl;
  int r = i;
  i = i0;
  while(i > 0) {
    i--;
    if(!from_left[i]) break;
  }
  int l = i + 1;
  vector<int> b;
  for(int i = l; i < r; i++) { b.push_back(a[i]); }
  sort(b.begin(), b.end());
  for(int i = l; i < r; i++) { a[i] = b[i - l]; }
  for(int i = 0; i < n; i++) { cout << a[i] << " \n"[i == n - 1]; }
}
