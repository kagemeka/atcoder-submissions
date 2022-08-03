#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  vector<int> idx(n);
  iota(idx.begin(), idx.end(), 0);
  sort(idx.begin(), idx.end(), [&](int i, int j) { return a[i] < a[j]; });
  vector<int> res(n);
  int b = -1;
  int pre = -1;
  for(int& i: idx) {
    int x = a[i];
    if(x != pre) b++;
    res[i] = b;
    pre = x;
  }
  for(int& x: res) cout << x << endl;
}
