#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int r, c, k, n;
  cin >> r >> c >> k >> n;
  vector<pair<int, int>> rc(n);
  vector<int> vert(r);
  vector<int> horz(c);
  for (int i = 0; i < n; i++) {
    int y, x;
    cin >> y >> x;
    y--; x--;
    rc[i] = pair<int, int>(y, x);
    vert[y]++;
    horz[x]++;
  }
  vector<int> cnt_v(k + 1);
  vector<int> cnt_h(k + 1);
  for (int i = 0; i < r; i++) {
    if (vert[i] > k) continue;
    cnt_v[vert[i]]++;
  }
  for (int i = 0; i < c; i++) {
    if (horz[i] > k) continue;
    cnt_h[horz[i]]++;
  }

  long long res = 0;
  for (int i = 0; i < k + 1; i++) {
    res += (long long)cnt_v[i] * cnt_h[k-i];
  }

  for (auto &p : rc) {
    auto &y = p.first;
    auto &x = p.second;
    int tmp = vert[y] + horz[x];
    res += tmp == k + 1;
    res -= tmp == k;
  }
  cout << res << '\n';
  return 0;
}
