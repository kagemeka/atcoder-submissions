#include <bits/stdc++.h>
using namespace std;

map<vector<int>, long long> comb;
long long choose(int n, int r) {
  if (r > n || r < 0) return 0;
  if (r == 0) return 1;
  if (comb.find({n, r}) != comb.end()) return comb[{n, r}];
  comb[{n, r}] = choose(n - 1, r) + choose(n - 1, r - 1);
  return comb[{n, r}];
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<string> s(n);
  for (int i = 0; i < n; i++) cin >> s[i];
  for (int i = 0; i < n; i++) {
    sort(s[i].begin(), s[i].end());
  }
  unordered_map<string, int> cnt;
  for (auto &t : s) {
    (cnt.find(t) != cnt.end()) ? cnt[t]++ : cnt[t] = 1;
  }
  long long tot = 0;
  for (auto &p : cnt) {
    tot += choose(p.second, 2);
  }
  cout << tot << '\n';
  return 0;
}
