#include <bits/stdc++.h>
using namespace std;

int bi_l(vector<int> vec, int val) {
  int l = -1, r = vec.size();
  while (l + 1 < r) {
    int m = (l + r) / 2;
    (vec[m] >= val) ? r = m : l = m;

  }
  return r;
}

int main() {
  int n;
  cin >> n;
  vector<int> c(n);
  for (int i = 0; i < n; i++) {
    cin >> c[i];
  }

  int INF = 100100;
  vector<int> res(n, INF);
  for (int x : c) {
    int i = bi_l(res, x);
    res[i] = x;
  }

  int ans = n - bi_l(res, INF);
  cout << ans << endl;
  return 0;
}
