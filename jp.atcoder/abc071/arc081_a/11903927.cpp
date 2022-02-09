#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  map<int, int, greater<int>> cnt;
  for (int i = 0; i < n; i++) {
    int a; cin >> a;
    (cnt.find(a) != cnt.end()) ? cnt[a]++ : cnt[a] = 1;
  }
  int y = 0, x = 0;
  for (auto &lc : cnt) {
    auto l = lc.first;
    auto c = lc.second / 2;
    if (!y && c) {y = l; c--;}
    if (!x && c) {x = l; break;}
  }
  cout << y * x << '\n';
  return 0;

}
