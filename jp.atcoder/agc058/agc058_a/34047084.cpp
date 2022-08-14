#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  int n2 = n << 1;
  vector<int> a(n2);
  for(int i = 0; i < n2; i++) cin >> a[i];
  int i = -1;
  vector<int> res;
  while(i < n2 - 2) {
    i++;
    if(i & 1) {
      // down
      if(a[i] > a[i + 1]) continue;
      if(a[i + 1] < a[i]) {
        swap(a[i], a[i + 1]);
        res.push_back(i);
        continue;
      } else {
        if(a[i] < a[i + 2]) {
          swap(a[i], a[i + 1]);
          res.push_back(i);
          continue;
        } else {
          swap(a[i + 1], a[i + 2]);
          res.push_back(i + 1);
          continue;
        }
      }
    } else {
      // up
      if(a[i] < a[i + 1]) continue;
      if(i == n2 - 2) {
        swap(a[i], a[i + 1]);
        res.push_back(i);
        continue;
      }
      if(a[i + 1] > a[i]) {
        swap(a[i], a[i + 1]);
        res.push_back(i);
        continue;
      } else {
        if(a[i] > a[i + 2]) {
          swap(a[i], a[i + 1]);
          res.push_back(i);
          continue;
        } else {
          swap(a[i + 1], a[i + 2]);
          res.push_back(i + 1);
          continue;
        }
      }
    }
  }
  n = res.size();
    cout << n << endl;
  for(int i = 0; i < n; i++) cout << res[i] + 1 << " \n"[i == n - 1];
}
