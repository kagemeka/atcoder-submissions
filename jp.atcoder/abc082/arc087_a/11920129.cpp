#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  unordered_map<int, int> cnt;
  for (int i = 0; i < n; i++) {
    int a; cin >> a;
    (cnt.find(a) != cnt.end()) ? cnt[a]++ : cnt[a] = 1;
  }
  int res = 0;
  for (auto vc : cnt) {
    int v = vc.first;
    int c = vc.second;
    res += (c < v) ? c : c - v;
  }
  cout << res << '\n';
  return 0;
}
